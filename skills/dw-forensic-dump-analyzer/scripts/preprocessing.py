# preprocessing.py — Forensic Dump Analyzer Utility Functions
# Run once at analysis start. All functions reusable across chunks.
# Usage: Copy this file to working directory and import, or run functions inline.

"""
Core utilities for the dw-forensic-dump-analyzer skill.
Consolidates all preprocessing, deduplication, size assessment,
baseline computation, and filtering functions into one place
so Claude doesn't re-implement them differently each run.
"""

import os
import glob
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path


# ============================================================
# 1. SIZE ASSESSMENT
# ============================================================

def assess_dump_size(file_paths):
    """Assess total data volume before loading. Returns (total_rows, total_size_mb, category_count)."""
    total_rows = 0
    total_size_mb = 0
    categories = set()

    for fp in file_paths:
        if not os.path.exists(fp):
            continue
        total_size_mb += os.path.getsize(fp) / (1024 * 1024)

        ext = Path(fp).suffix.lower()
        if ext == '.csv':
            try:
                total_rows += sum(1 for _ in open(fp, errors='ignore')) - 1
            except Exception:
                pass
        elif ext in ('.xlsx', '.xls'):
            try:
                total_rows += len(pd.read_excel(fp))
            except Exception:
                pass
        elif ext in ('.html', '.htm'):
            try:
                tables = pd.read_html(fp)
                total_rows += sum(len(t) for t in tables)
            except Exception:
                pass

        # Classify category from filename/path
        name_lower = Path(fp).stem.lower()
        # Also check full path for folder-based classification
        path_lower = str(fp).lower()
        for keyword, cat in [
            # SMS/iMessage/RCS — platform-specific messaging (Note: 'message' requires platform-specific parsing)
            ('imessage', 'iMessage'), ('rcs', 'RCS'), ('sms', 'SMS'), ('mms', 'SMS'),
            ('message', 'Messages'),  # Placeholder; requires further classification by platform
            ('chat', 'Chat'), ('whatsapp', 'Chat'), ('signal', 'Chat'), ('telegram', 'Chat'),
            ('messenger', 'Chat'), ('instagram', 'Chat'),
            ('call', 'Calls'), ('voicemail', 'Calls'),
            ('sim', 'SIM'), ('iccid', 'SIM'), ('imsi', 'SIM'), ('sim_card', 'SIM'),
            ('contact', 'Contacts'),
            ('location', 'Location'), ('gps', 'Location'), ('tower', 'Location'),
            ('wifi', 'Location'), ('kml', 'Location'),
            ('wifi_connection', 'WiFi'), ('wireless_network', 'WiFi'), ('wifi_log', 'WiFi'), ('ssid', 'WiFi'),
            ('photo', 'Photos'), ('image', 'Photos'), ('screenshot', 'Photos'),
            ('video', 'Videos'), ('recording', 'Videos'), ('screen_rec', 'Videos'),
            ('dcim', 'Photos'), ('camera', 'Photos'),
            ('notification', 'Notifications'), ('push_notification', 'Notifications'), ('alert', 'Notifications'),
            ('cashapp', 'Financial'), ('venmo', 'Financial'), ('zelle', 'Financial'),
            ('paypal', 'Financial'), ('cash_app', 'Financial'), ('transaction', 'Financial'),
            ('health', 'Health'), ('fitness', 'Health'), ('step', 'Health'),
            ('heart_rate', 'Health'), ('workout', 'Health'),
            ('voice_memo', 'PersonalApps'), ('voicememo', 'PersonalApps'),
            ('note', 'PersonalApps'), ('calendar', 'PersonalApps'),
            ('reminder', 'PersonalApps'), ('email', 'PersonalApps'),
            ('browser', 'Browser'), ('history', 'Browser'), ('search', 'Browser'),
            ('screen_time', 'AppUsage'), ('app_usage', 'AppUsage'), ('application_usage', 'AppUsage'),
            ('foreground', 'AppUsage'), ('screentime', 'AppUsage'), ('usage_stats', 'AppUsage'), ('battery_usage', 'AppUsage'),
            ('keyboard', 'KeyboardArtifacts'), ('autocorrect', 'KeyboardArtifacts'), ('clipboard', 'KeyboardArtifacts'),
            ('dictionary', 'KeyboardArtifacts'), ('typing', 'KeyboardArtifacts'), ('user_dictionary', 'KeyboardArtifacts'),
            ('predictive', 'KeyboardArtifacts'),
            ('app', 'Apps'), ('install', 'Apps'),
            ('system', 'System'), ('log', 'System'), ('power', 'System'),
            # Cellebrite database filenames (iOS)
            ('sms.db', 'SMS'), ('mobilesms', 'SMS'), ('com.apple.mobilesms', 'SMS'),
            ('callhistory.storedata', 'Calls'), ('call_history', 'Calls'),
            ('addressbook', 'Contacts'), ('contacts2.db', 'Contacts'), ('com.apple.addressbook', 'Contacts'),
            ('photos.sqlite', 'Photos'), ('com.apple.photos', 'Photos'),
            ('cache_encryptedB.db', 'Browser'), ('safari', 'Browser'), ('chrome', 'Browser'),
            ('locationd', 'Location'), ('routined', 'Location'), ('com.apple.routined', 'Location'),
            ('healthdb', 'Health'), ('health.sqlite', 'Health'), ('com.apple.health', 'Health'),
            ('calendar.sqlitedb', 'PersonalApps'), ('com.apple.mobilecal', 'PersonalApps'),
            ('notes.sqlite', 'PersonalApps'), ('com.apple.notes', 'PersonalApps'),
            # Cellebrite database filenames (Android)
            ('mmssms.db', 'SMS'), ('telephony', 'SMS'),
            ('com.android.contacts', 'Contacts'),
            ('calllog', 'Calls'), ('com.android.providers.call', 'Calls'),
            ('external.db', 'Photos'), ('com.android.providers.media', 'Photos'),
            ('browser2.db', 'Browser'), ('com.android.browser', 'Browser'),
            ('com.google.android.gms', 'Location'),
            # Common Cellebrite export naming patterns
            ('analyzed_chat', 'Chat'), ('instant_message', 'Chat'),
            ('web_history', 'Browser'), ('web_bookmark', 'Browser'),
            ('installed_app', 'Apps'), ('user_account', 'Apps'),
            ('device_event', 'System'), ('power_event', 'System'),
            ('bluetooth', 'System'), ('wireless', 'Location'),
        ]:
            if keyword in name_lower or keyword in path_lower:
                categories.add(cat)
                break

    return total_rows, round(total_size_mb, 2), len(categories)


def should_chunk(total_rows, total_size_mb, category_count):
    """Returns 'single-pass', 'chunked', or 'always-chunk'."""
    if category_count >= 5:
        return 'always-chunk'
    if total_rows >= 15000 or total_size_mb > 2.0 or category_count > 3:
        return 'chunked'
    return 'single-pass'


# ============================================================
# 2. DEDUPLICATION
# ============================================================

def deduplicate_records(df, subset_cols=None):
    """
    Deduplicate records. Returns (deduped_df, duplicate_count).
    Marks duplicates rather than removing — preserves for verification.
    Default dedup columns: timestamp, content, sender, recipient.
    Adapts if columns don't exist.
    """
    if subset_cols is None:
        available = [c for c in ['timestamp', 'content', 'sender', 'recipient',
                                  'body', 'text', 'message', 'from', 'to',
                                  'date', 'time'] if c in df.columns]
        if len(available) < 2:
            # Not enough columns to deduplicate meaningfully
            return df, 0
        subset_cols = available

    before = len(df)
    df = df.copy()
    df['_is_duplicate'] = df.duplicated(subset=subset_cols, keep='first')
    dup_count = df['_is_duplicate'].sum()
    return df, dup_count


def classify_message_platform(df):
    """
    Classify messages by platform (SMS, MMS, iMessage, RCS, FB Messenger, WhatsApp, Instagram DM, Signal, Telegram, Other).

    Takes a dataframe of messages and looks for platform indicators in columns like:
    'source', 'application', 'type', 'service', 'account', 'platform', 'app', 'from_app', 'message_type'.

    Returns the dataframe with a new '_platform' column containing platform classification.

    **WHY THIS MATTERS FOR DEFENSE:**

    iMessage (Apple) sends "Delivered" and "Read" receipts that are cryptographically signed,
    timestamped, and independently verifiable. These receipts prove not just that a message was
    sent, but that it was RECEIVED and READ at a specific time. This is powerful exculpatory evidence
    if the defendant can prove they read a message at a time inconsistent with prosecution narrative.

    RCS (Android's advanced messaging) includes typing indicators and read receipts, though not as
    robust as iMessage's end-to-end encrypted receipts.

    SMS and MMS have NO delivery confirmations, NO read receipts, NO typing indicators. They are
    unreliable — a message may fail silently, and there is no way to prove receipt without independent
    evidence (e.g., defendant's testimony, reply message).

    Prosecution often conflates these platforms when building narratives about "message frequency"
    or "read receipts" to suggest awareness or coordination. NEVER let them bundle SMS, iMessage,
    and RCS together without noting the fundamental differences in receipt/read capabilities.
    A "read receipt" claim is worth nothing if the message was sent via SMS.
    """
    df = df.copy()

    # Define platform keywords and their mappings
    platform_keywords = {
        'iMessage': ['imessage', 'iphonedevice', 'iphone', 'apple message', 'apple_messaging'],
        'RCS': ['rcs', 'android rcs', 'rich communication', 'google messages', 'googlemessages'],
        'SMS': ['sms', 'short message service', 'plain sms', 'standard sms'],
        'MMS': ['mms', 'multimedia message', 'picture message', 'video message'],
        'WhatsApp': ['whatsapp', 'whatsapp messenger'],
        'Signal': ['signal', 'signal messenger'],
        'Telegram': ['telegram', 'telegram messenger'],
        'FB Messenger': ['facebook messenger', 'fb messenger', 'messenger', 'fbmessenger'],
        'Instagram DM': ['instagram', 'instagram direct', 'insta dm', 'instagram dm'],
    }

    # List of columns to check for platform indicators
    indicator_cols = [c for c in ['source', 'application', 'type', 'service', 'account',
                                    'platform', 'app', 'from_app', 'message_type', 'service_name',
                                    'app_name', 'category'] if c in df.columns]

    def detect_platform(row):
        """Detect platform from available indicator columns."""
        # Concatenate all indicator columns into a single searchable string
        search_text = ' '.join([str(row.get(col, '')).lower() for col in indicator_cols])

        # Check each platform's keywords
        for platform, keywords in platform_keywords.items():
            for keyword in keywords:
                if keyword in search_text:
                    return platform

        return 'Other'

    df['_platform'] = df.apply(detect_platform, axis=1)
    return df


# ============================================================
# 3. DATE FILTERING
# ============================================================

def filter_to_window(df, timestamp_col, window_start, window_end):
    """Filter dataframe to a date/time window. Returns filtered df."""
    df = df.copy()
    df[timestamp_col] = pd.to_datetime(df[timestamp_col], errors='coerce')
    mask = (df[timestamp_col] >= pd.Timestamp(window_start)) & \
           (df[timestamp_col] <= pd.Timestamp(window_end))
    return df[mask]


def filter_critical_window(df, timestamp_col, crime_datetime, buffer_hours=48):
    """Filter to critical window: crime datetime ± buffer."""
    crime_dt = pd.Timestamp(crime_datetime)
    start = crime_dt - timedelta(hours=buffer_hours)
    end = crime_dt + timedelta(hours=buffer_hours)
    return filter_to_window(df, timestamp_col, start, end)


# ============================================================
# 4. PATTERN OF LIFE BASELINE
# ============================================================

def compute_baseline(df, timestamp_col, baseline_start, baseline_end):
    """
    Compute Pattern of Life baseline metrics.
    Returns dict with all baseline values.
    """
    df = df.copy()
    df[timestamp_col] = pd.to_datetime(df[timestamp_col], errors='coerce')
    bl = df[(df[timestamp_col] >= pd.Timestamp(baseline_start)) &
            (df[timestamp_col] < pd.Timestamp(baseline_end))].copy()

    if len(bl) == 0:
        return {'error': 'No data in baseline period'}

    bl['_date'] = bl[timestamp_col].dt.date
    bl['_hour'] = bl[timestamp_col].dt.hour

    # Daily volume
    daily = bl.groupby('_date').size()

    # Hourly pattern
    hourly = bl.groupby('_hour').size()
    active_hours = hourly[hourly > hourly.quantile(0.25)].index.tolist()

    # Contact frequency (if contact column exists)
    contact_col = next((c for c in ['contact', 'sender', 'recipient', 'from', 'to', 'number']
                        if c in bl.columns), None)
    top_contacts = {}
    if contact_col:
        top_contacts = bl[contact_col].value_counts().head(5).to_dict()

    # Gap detection
    bl_sorted = bl.sort_values(timestamp_col)
    if len(bl_sorted) > 1:
        gaps = bl_sorted[timestamp_col].diff().dt.total_seconds() / 3600
        normal_gap_hours = gaps.median()
    else:
        normal_gap_hours = None

    return {
        'period': f"{baseline_start} to {baseline_end}",
        'daily_avg': round(daily.mean(), 1),
        'daily_std': round(daily.std(), 1),
        'active_hours': f"{min(active_hours)}:00–{max(active_hours)}:00" if active_hours else 'N/A',
        'top_contacts': top_contacts,
        'normal_gap_hours': round(normal_gap_hours, 1) if normal_gap_hours else 'N/A',
        'total_records': len(bl),
        'days_sampled': len(daily),
    }


def compare_to_baseline(baseline, critical_window_df, timestamp_col):
    """Compare critical window activity against baseline. Returns deviations."""
    cw = critical_window_df.copy()
    cw[timestamp_col] = pd.to_datetime(cw[timestamp_col], errors='coerce')

    if len(cw) == 0:
        return {'deviation': 'No data in critical window'}

    cw['_date'] = cw[timestamp_col].dt.date
    cw_daily = cw.groupby('_date').size()

    deviations = {}
    if isinstance(baseline.get('daily_avg'), (int, float)):
        cw_avg = cw_daily.mean()
        bl_avg = baseline['daily_avg']
        bl_std = baseline.get('daily_std', 1)
        if bl_std > 0:
            z_score = (cw_avg - bl_avg) / bl_std
            if abs(z_score) > 2:
                deviations['daily_volume'] = f"UNUSUAL: {cw_avg:.0f}/day vs baseline {bl_avg}/day (z={z_score:.1f})"
            else:
                deviations['daily_volume'] = f"NORMAL: {cw_avg:.0f}/day vs baseline {bl_avg}/day"

    return deviations


# ============================================================
# 5. CELLEBRITE HTML CONVERSION
# ============================================================

def cellebrite_html_to_csv(html_path, output_dir):
    """Convert Cellebrite HTML report tables to CSV files. Returns list of CSV paths."""
    try:
        tables = pd.read_html(html_path)
    except Exception as e:
        return [f"Error parsing HTML: {e}"]

    csv_paths = []
    stem = Path(html_path).stem
    for i, table in enumerate(tables):
        if len(table) < 2:
            continue
        csv_path = os.path.join(output_dir, f"{stem}_table_{i}.csv")
        table.to_csv(csv_path, index=False)
        csv_paths.append(csv_path)
    return csv_paths


# ============================================================
# 6. FREQUENCY ANALYSIS (with baseline comparison)
# ============================================================

def contact_frequency_analysis(df, contact_col, timestamp_col, baseline_start, baseline_end, critical_start, critical_end):
    """
    Compare contact frequency between baseline and critical window.
    ALWAYS use this before claiming any contact frequency is 'high' or 'unusual'.
    """
    df = df.copy()
    df[timestamp_col] = pd.to_datetime(df[timestamp_col], errors='coerce')

    baseline = df[(df[timestamp_col] >= pd.Timestamp(baseline_start)) &
                  (df[timestamp_col] < pd.Timestamp(baseline_end))]
    critical = df[(df[timestamp_col] >= pd.Timestamp(critical_start)) &
                  (df[timestamp_col] <= pd.Timestamp(critical_end))]

    bl_days = max((pd.Timestamp(baseline_end) - pd.Timestamp(baseline_start)).days, 1)
    cw_days = max((pd.Timestamp(critical_end) - pd.Timestamp(critical_start)).days, 1)

    bl_freq = (baseline.groupby(contact_col).size() / bl_days).to_dict()
    cw_freq = (critical.groupby(contact_col).size() / cw_days).to_dict()

    results = []
    all_contacts = set(list(bl_freq.keys()) + list(cw_freq.keys()))
    for contact in all_contacts:
        bl_rate = bl_freq.get(contact, 0)
        cw_rate = cw_freq.get(contact, 0)
        change = 'NEW' if bl_rate == 0 and cw_rate > 0 else \
                 'GONE' if bl_rate > 0 and cw_rate == 0 else \
                 'SPIKE' if cw_rate > bl_rate * 2 else \
                 'DROP' if cw_rate < bl_rate * 0.5 else 'NORMAL'
        if change != 'NORMAL':
            results.append({
                'contact': contact,
                'baseline_per_day': round(bl_rate, 2),
                'critical_per_day': round(cw_rate, 2),
                'change': change
            })

    return sorted(results, key=lambda x: abs(x.get('critical_per_day', 0) - x.get('baseline_per_day', 0)), reverse=True)


# ============================================================
# 7. SHARED DEVICE DETECTION
# ============================================================

def detect_shared_device(df, timestamp_col, content_col=None, confirmed_absence_periods=None):
    """
    Check for indicators of multiple users on the same device.
    confirmed_absence_periods: list of (start, end) tuples when defendant was confirmed elsewhere.
    """
    indicators = []
    df = df.copy()
    df[timestamp_col] = pd.to_datetime(df[timestamp_col], errors='coerce')

    # Check for activity during confirmed absence
    if confirmed_absence_periods:
        for start, end in confirmed_absence_periods:
            activity = df[(df[timestamp_col] >= pd.Timestamp(start)) &
                          (df[timestamp_col] <= pd.Timestamp(end))]
            if len(activity) > 0:
                indicators.append(f"ACTIVITY DURING CONFIRMED ABSENCE: {len(activity)} records between {start} and {end}")

    return indicators


# ============================================================
# 8. VIDEO INTELLIGENCE
# ============================================================

def inventory_video_files(file_paths):
    """
    Catalog all video files found in the extraction.
    Returns a list of dicts with metadata for each video.
    Video files on phones are goldmines: they have timestamps, GPS,
    duration (proves someone was recording for X minutes at Y location),
    audio tracks, and content that can establish alibi or contradict
    the State's narrative.
    """
    VIDEO_EXTENSIONS = {'.mp4', '.mov', '.m4v', '.3gp', '.3gpp', '.avi',
                        '.mkv', '.webm', '.wmv', '.flv', '.ts'}
    videos = []

    for fp in file_paths:
        ext = Path(fp).suffix.lower()
        if ext not in VIDEO_EXTENSIONS:
            continue

        stat = os.stat(fp) if os.path.exists(fp) else None
        name_lower = Path(fp).name.lower()

        # Classify video type from filename/path patterns
        video_type = 'unknown'
        path_lower = str(fp).lower()
        if any(k in path_lower for k in ['dcim', 'camera', 'cam']):
            video_type = 'camera_recording'
        elif any(k in path_lower for k in ['screen_rec', 'screenrec', 'screen recording']):
            video_type = 'screen_recording'
        elif any(k in path_lower for k in ['download', 'received']):
            video_type = 'received'
        elif any(k in path_lower for k in ['whatsapp', 'telegram', 'signal', 'messenger']):
            video_type = 'chat_media'
        elif any(k in path_lower for k in ['snapchat', 'instagram', 'tiktok']):
            video_type = 'social_media'
        elif 'voice' in path_lower or 'memo' in path_lower:
            video_type = 'voice_video_memo'
        elif 'live' in name_lower or 'img_' in name_lower:
            video_type = 'live_photo_video'

        videos.append({
            'path': str(fp),
            'filename': Path(fp).name,
            'extension': ext,
            'size_mb': round(stat.st_size / (1024 * 1024), 2) if stat else 0,
            'modified': datetime.fromtimestamp(stat.st_mtime).isoformat() if stat else None,
            'video_type': video_type,
        })

    return sorted(videos, key=lambda v: v.get('modified') or '', reverse=True)


def extract_video_metadata(video_path):
    """
    Extract EXIF/metadata from a video file using available tools.
    Returns dict of metadata fields. Tries ffprobe first (most reliable
    for video), falls back to PIL for container metadata.
    """
    import subprocess
    import json as json_module

    metadata = {'path': video_path, 'filename': Path(video_path).name}

    # Try ffprobe (most reliable for video metadata)
    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'quiet', '-print_format', 'json',
             '-show_format', '-show_streams', video_path],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            probe = json_module.loads(result.stdout)

            # Format-level metadata
            fmt = probe.get('format', {})
            metadata['duration_seconds'] = float(fmt.get('duration', 0))
            metadata['duration_human'] = _seconds_to_human(metadata['duration_seconds'])
            metadata['size_mb'] = round(float(fmt.get('size', 0)) / (1024 * 1024), 2)
            metadata['format'] = fmt.get('format_long_name', '')
            metadata['creation_time'] = fmt.get('tags', {}).get('creation_time', '')

            # GPS from tags (common in iPhone/Android recordings)
            tags = fmt.get('tags', {})
            for key in ['com.apple.quicktime.location.ISO6709', 'location',
                        'com.android.capture.gps_latitude']:
                if key in tags:
                    metadata['gps_raw'] = tags[key]
                    break

            # Stream info (video + audio)
            for stream in probe.get('streams', []):
                if stream.get('codec_type') == 'video':
                    metadata['video_codec'] = stream.get('codec_name', '')
                    metadata['resolution'] = f"{stream.get('width', '?')}x{stream.get('height', '?')}"
                    metadata['frame_rate'] = stream.get('r_frame_rate', '')
                elif stream.get('codec_type') == 'audio':
                    metadata['has_audio'] = True
                    metadata['audio_codec'] = stream.get('codec_name', '')
                    metadata['audio_channels'] = stream.get('channels', 0)

            if 'has_audio' not in metadata:
                metadata['has_audio'] = False

    except (FileNotFoundError, subprocess.TimeoutExpired, Exception):
        # ffprobe not available — fall back to file size/mtime only
        try:
            stat = os.stat(video_path)
            metadata['size_mb'] = round(stat.st_size / (1024 * 1024), 2)
            metadata['modified'] = datetime.fromtimestamp(stat.st_mtime).isoformat()
        except Exception:
            pass

    return metadata


def _seconds_to_human(seconds):
    """Convert seconds to human-readable duration string."""
    if seconds <= 0:
        return "0s"
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    parts = []
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    if secs or not parts:
        parts.append(f"{secs}s")
    return " ".join(parts)


def build_video_timeline(video_metadata_list, critical_start=None, critical_end=None):
    """
    Build a chronological timeline of all videos.
    If critical_start/critical_end provided, flags videos within the crime window.
    A video recorded during the critical window is potentially powerful:
    - Its timestamp + duration proves the phone owner was recording for X minutes
    - GPS metadata places them at a specific location
    - Audio track captures ambient sound (voices, environment)
    - Content may directly show what was happening
    """
    timeline = []
    for vm in video_metadata_list:
        creation = vm.get('creation_time') or vm.get('modified')
        if not creation:
            continue

        entry = {
            'filename': vm['filename'],
            'timestamp': creation,
            'duration': vm.get('duration_human', 'unknown'),
            'duration_seconds': vm.get('duration_seconds', 0),
            'has_gps': bool(vm.get('gps_raw')),
            'has_audio': vm.get('has_audio', False),
            'video_type': vm.get('video_type', 'unknown'),
            'resolution': vm.get('resolution', 'unknown'),
        }

        # Flag if in critical window
        if critical_start and critical_end:
            try:
                ts = pd.Timestamp(creation)
                cs = pd.Timestamp(critical_start)
                ce = pd.Timestamp(critical_end)
                entry['in_critical_window'] = cs <= ts <= ce
            except Exception:
                entry['in_critical_window'] = False
        else:
            entry['in_critical_window'] = False

        timeline.append(entry)

    return sorted(timeline, key=lambda x: x.get('timestamp', ''))


# ============================================================
# 10. WI-FI CONNECTION ANALYSIS
# ============================================================

def analyze_wifi_connections(df, timestamp_col=None, ssid_col=None):
    """
    Analyze Wi-Fi connection history for defense intelligence.
    Cellebrite extracts saved Wi-Fi networks with connection timestamps
    under Device Information > Wireless Networks.

    Wi-Fi connections are powerful alibi evidence:
    - Connection to home Wi-Fi = phone was at home
    - Connection to work Wi-Fi = phone was at work
    - Connection to Starbucks Wi-Fi = phone was at that Starbucks
    - Disconnect timestamp = phone left that location

    Unlike GPS (which can be spotty indoors), Wi-Fi connections are
    reliable indoor location indicators.
    """
    # Auto-detect columns
    if timestamp_col is None:
        timestamp_col = next((c for c in df.columns if any(k in c.lower()
            for k in ['timestamp', 'time', 'date', 'connected', 'last_seen'])), None)
    if ssid_col is None:
        ssid_col = next((c for c in df.columns if any(k in c.lower()
            for k in ['ssid', 'network', 'name', 'wifi'])), None)

    if not ssid_col:
        return {'error': 'Could not identify SSID/network column', 'columns': list(df.columns)}

    result = {
        'total_networks': df[ssid_col].nunique(),
        'total_connections': len(df),
        'networks': {},
    }

    # Classify networks by likely location type
    for ssid in df[ssid_col].unique():
        ssid_lower = str(ssid).lower()
        location_type = 'unknown'
        if any(k in ssid_lower for k in ['home', 'house', 'apt', 'apartment', 'mynetwork', 'netgear', 'linksys', 'xfinity', 'att', 'spectrum']):
            location_type = 'likely_home'
        elif any(k in ssid_lower for k in ['office', 'corp', 'work', 'company', 'enterprise']):
            location_type = 'likely_work'
        elif any(k in ssid_lower for k in ['starbucks', 'mcdonalds', 'hotel', 'airport', 'guest', 'free', 'public']):
            location_type = 'commercial_venue'
        elif any(k in ssid_lower for k in ['school', 'university', 'library', 'hospital']):
            location_type = 'institution'

        network_data = df[df[ssid_col] == ssid]
        result['networks'][str(ssid)] = {
            'connections': len(network_data),
            'location_type': location_type,
        }
        if timestamp_col and timestamp_col in df.columns:
            times = pd.to_datetime(network_data[timestamp_col], errors='coerce').dropna()
            if len(times) > 0:
                result['networks'][str(ssid)]['first_seen'] = str(times.min())
                result['networks'][str(ssid)]['last_seen'] = str(times.max())

    return result


# ============================================================
# 11. PHOTO EXIF METADATA EXTRACTION
# ============================================================

def extract_photo_metadata(image_path):
    """
    Extract EXIF metadata from a photo file.
    Returns dict with GPS coordinates, camera model, timestamps,
    orientation, and other forensically relevant fields.

    Photos are the most common media type in phone dumps. Their EXIF
    data can prove: WHERE a photo was taken (GPS), WHEN (timestamps),
    WITH WHAT device (camera model — proves origin), and whether
    the photo was modified (software tags, edit history).

    Uses PIL/Pillow which is available in the analysis environment.
    Falls back to basic file stats if PIL is unavailable.
    """
    from pathlib import Path
    metadata = {'path': str(image_path), 'filename': Path(image_path).name}

    try:
        from PIL import Image
        from PIL.ExifTags import TAGS, GPSTAGS

        img = Image.open(image_path)
        exif_data = img._getexif()

        if exif_data is None:
            metadata['exif_present'] = False
            metadata['defense_note'] = 'No EXIF data — photo may have been stripped (social media pipeline), screenshotted, or received via messaging app'
            # Still get basic info
            metadata['dimensions'] = f"{img.width}x{img.height}"
            metadata['format'] = img.format
            return metadata

        metadata['exif_present'] = True

        # Parse all EXIF tags
        parsed = {}
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            parsed[tag_name] = value

        # Key forensic fields
        metadata['camera_make'] = parsed.get('Make', '')
        metadata['camera_model'] = parsed.get('Model', '')
        metadata['software'] = parsed.get('Software', '')
        metadata['datetime_original'] = str(parsed.get('DateTimeOriginal', ''))
        metadata['datetime_digitized'] = str(parsed.get('DateTimeDigitized', ''))
        metadata['datetime_modified'] = str(parsed.get('DateTime', ''))
        metadata['orientation'] = parsed.get('Orientation', '')
        metadata['dimensions'] = f"{img.width}x{img.height}"
        metadata['format'] = img.format

        # GPS extraction
        gps_info = parsed.get('GPSInfo', {})
        if gps_info:
            gps_parsed = {}
            for key, val in gps_info.items():
                gps_tag = GPSTAGS.get(key, key)
                gps_parsed[gps_tag] = val

            metadata['has_gps'] = True

            # Convert GPS coordinates to decimal degrees
            try:
                lat = gps_parsed.get('GPSLatitude', ())
                lat_ref = gps_parsed.get('GPSLatitudeRef', 'N')
                lon = gps_parsed.get('GPSLongitude', ())
                lon_ref = gps_parsed.get('GPSLongitudeRef', 'E')

                if lat and lon:
                    lat_decimal = float(lat[0]) + float(lat[1]) / 60 + float(lat[2]) / 3600
                    lon_decimal = float(lon[0]) + float(lon[1]) / 60 + float(lon[2]) / 3600
                    if lat_ref == 'S':
                        lat_decimal = -lat_decimal
                    if lon_ref == 'W':
                        lon_decimal = -lon_decimal
                    metadata['gps_latitude'] = round(lat_decimal, 6)
                    metadata['gps_longitude'] = round(lon_decimal, 6)
            except (TypeError, ValueError, IndexError, ZeroDivisionError):
                metadata['gps_parse_error'] = True

            metadata['gps_altitude'] = gps_parsed.get('GPSAltitude', '')
            metadata['gps_timestamp'] = str(gps_parsed.get('GPSTimeStamp', ''))
            metadata['gps_date'] = str(gps_parsed.get('GPSDateStamp', ''))
        else:
            metadata['has_gps'] = False

        # MediaOrigin / Capturing Device analysis
        # If camera make/model matches the extraction device, it was taken BY this phone
        # If different or absent, it was received/downloaded
        if metadata['camera_make'] or metadata['camera_model']:
            metadata['origin_assessment'] = 'HAS_DEVICE_INFO — compare against extraction device to determine if taken by this phone or another device'
        else:
            metadata['origin_assessment'] = 'NO_DEVICE_INFO — likely screenshot, received image, or social media download'

    except ImportError:
        # PIL not available — fall back to file stats
        import os
        try:
            stat = os.stat(image_path)
            metadata['size_mb'] = round(stat.st_size / (1024 * 1024), 2)
            metadata['modified'] = datetime.fromtimestamp(stat.st_mtime).isoformat()
            metadata['exif_present'] = None
            metadata['defense_note'] = 'PIL/Pillow not available — install with: pip install Pillow'
        except Exception:
            pass
    except Exception as e:
        metadata['error'] = str(e)

    return metadata


def batch_photo_metadata(file_paths, device_make=None, device_model=None):
    """
    Extract metadata from multiple photos and classify by origin.
    If device_make/device_model provided, classifies each photo as:
    - 'taken_by_device': Camera make/model matches extraction device
    - 'taken_by_other': Different camera — taken by another device
    - 'received_or_downloaded': No EXIF or stripped metadata
    - 'screenshot': Matches screenshot naming patterns or dimensions

    Returns list of metadata dicts sorted by timestamp.
    """
    IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.heic', '.heif', '.tiff', '.bmp', '.webp', '.gif'}

    results = []
    for fp in file_paths:
        ext = Path(fp).suffix.lower()
        if ext not in IMAGE_EXTENSIONS:
            continue

        meta = extract_photo_metadata(fp)

        # Origin classification
        if 'screenshot' in Path(fp).name.lower() or \
           any(k in str(fp).lower() for k in ['screenshot', 'screen_shot', 'screen shot']):
            meta['origin'] = 'screenshot'
        elif not meta.get('exif_present'):
            meta['origin'] = 'received_or_downloaded'
        elif device_make and device_model:
            if (device_make.lower() in str(meta.get('camera_make', '')).lower() and
                device_model.lower() in str(meta.get('camera_model', '')).lower()):
                meta['origin'] = 'taken_by_device'
            elif meta.get('camera_make') or meta.get('camera_model'):
                meta['origin'] = 'taken_by_other'
            else:
                meta['origin'] = 'received_or_downloaded'
        else:
            meta['origin'] = 'unknown_no_device_reference'

        results.append(meta)

    # Sort by original datetime if available
    return sorted(results, key=lambda x: x.get('datetime_original') or x.get('datetime_modified') or '', reverse=True)


def photos_in_critical_window(photo_metadata_list, critical_start, critical_end):
    """
    Filter photos to those taken during the critical window.
    A photo taken during the crime window with GPS coordinates is
    alibi evidence — it places the phone at a specific location at a specific time.
    """
    import pandas as pd

    cs = pd.Timestamp(critical_start)
    ce = pd.Timestamp(critical_end)

    critical_photos = []
    for meta in photo_metadata_list:
        timestamp = meta.get('datetime_original') or meta.get('datetime_modified')
        if not timestamp:
            continue
        try:
            ts = pd.Timestamp(timestamp)
            if cs <= ts <= ce:
                meta['in_critical_window'] = True
                meta['defense_value'] = 'CRITICAL WINDOW PHOTO'
                if meta.get('has_gps'):
                    meta['defense_value'] += f" — GPS VERIFIED at ({meta.get('gps_latitude')}, {meta.get('gps_longitude')})"
                critical_photos.append(meta)
        except Exception:
            continue

    return sorted(critical_photos, key=lambda x: x.get('datetime_original') or '')


# ============================================================
# 9. APPLICATION USAGE / SCREEN TIME
# ============================================================

def parse_app_usage(df, timestamp_col=None, app_col=None, duration_col=None):
    """
    Parse application usage data from Cellebrite extraction.
    Cellebrite exports this under Device Information > Application Usage.
    Fields typically include: app name, launch time, foreground duration, termination time.

    This data is GOLD for alibi timelines — it proves the phone owner was actively
    using a specific app at a specific time for a specific duration. Unlike passive
    data (messages received), app usage requires active user engagement.

    Returns dict with: total_apps, usage_by_app, critical_window_usage, screen_on_periods
    """
    # Auto-detect column names
    if timestamp_col is None:
        timestamp_col = next((c for c in df.columns if any(k in c.lower() for k in ['timestamp', 'launch', 'start', 'time', 'date'])), None)
    if app_col is None:
        app_col = next((c for c in df.columns if any(k in c.lower() for k in ['app', 'application', 'bundle', 'package', 'name'])), None)
    if duration_col is None:
        duration_col = next((c for c in df.columns if any(k in c.lower() for k in ['duration', 'foreground', 'usage', 'active'])), None)

    if not timestamp_col or not app_col:
        return {'error': 'Could not identify timestamp or app columns', 'columns_found': list(df.columns)}

    result = {
        'total_records': len(df),
        'unique_apps': df[app_col].nunique() if app_col else 0,
        'date_range': None,
        'top_apps_by_usage': {},
    }

    if timestamp_col:
        df = df.copy()
        df[timestamp_col] = pd.to_datetime(df[timestamp_col], errors='coerce')
        valid = df[df[timestamp_col].notna()]
        if len(valid) > 0:
            result['date_range'] = f"{valid[timestamp_col].min()} to {valid[timestamp_col].max()}"

    if app_col:
        result['top_apps_by_usage'] = df[app_col].value_counts().head(20).to_dict()

    return result


def app_usage_critical_window(df, timestamp_col, app_col, critical_start, critical_end, duration_col=None):
    """
    Extract all app usage during the critical window.
    Returns a chronological list of app sessions — each one proves
    the phone was in active use at that time.
    """
    df = df.copy()
    df[timestamp_col] = pd.to_datetime(df[timestamp_col], errors='coerce')

    mask = (df[timestamp_col] >= pd.Timestamp(critical_start)) & \
           (df[timestamp_col] <= pd.Timestamp(critical_end))
    cw = df[mask].sort_values(timestamp_col)

    sessions = []
    for _, row in cw.iterrows():
        session = {
            'app': row[app_col],
            'time': str(row[timestamp_col]),
            'defense_value': 'ACTIVE PHONE USE — proves user engagement'
        }
        if duration_col and duration_col in row.index:
            session['duration'] = row[duration_col]
        sessions.append(session)

    return sessions


# ============================================================
# UFDR FILE EXTRACTION
# ============================================================

def detect_ufdr(file_paths):
    """
    Check if any uploaded files are UFDR containers.
    Returns list of UFDR file paths found.
    UFDR files are Cellebrite's native export format — essentially
    ZIP archives containing HTML reports, media files, and optionally
    raw SQLite databases.
    """
    ufdr_files = []
    for fp in file_paths:
        fp_str = str(fp)
        # Check extension
        if fp_str.lower().endswith('.ufdr'):
            ufdr_files.append(fp_str)
            continue
        # Some UFDRs are renamed or have no extension — check ZIP magic bytes
        try:
            with open(fp_str, 'rb') as f:
                magic = f.read(4)
                if magic == b'PK\x03\x04':  # ZIP magic number
                    # Could be a UFDR — check for Cellebrite markers inside
                    import zipfile
                    if zipfile.is_zipfile(fp_str):
                        with zipfile.ZipFile(fp_str, 'r') as zf:
                            names = zf.namelist()
                            # UFDR typically contains report files and a files/ directory
                            if any('report' in n.lower() for n in names) or \
                               any('files/' in n for n in names) or \
                               any('.html' in n.lower() for n in names):
                                ufdr_files.append(fp_str)
        except (IOError, OSError, Exception):
            pass
    return ufdr_files


def extract_ufdr(ufdr_path, output_dir=None):
    """
    Extract a UFDR file to a working directory.
    Returns dict with paths to extracted components:
    - 'html_reports': list of HTML report files
    - 'media_files': list of extracted media (photos, videos, audio)
    - 'databases': list of SQLite database files
    - 'output_dir': the extraction directory
    - 'total_files': count of all extracted files

    IMPORTANT: If databases are found, flag for dw-sqlite-recovery
    handoff — WAL analysis should happen before repeated file access.
    """
    import zipfile

    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(ufdr_path),
                                   Path(ufdr_path).stem + '_extracted')

    os.makedirs(output_dir, exist_ok=True)

    result = {
        'output_dir': output_dir,
        'html_reports': [],
        'csv_files': [],
        'media_files': [],
        'databases': [],
        'other_files': [],
        'total_files': 0,
        'sqlite_recovery_needed': False,
    }

    MEDIA_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.heic', '.heif', '.mp4', '.mov',
                        '.m4v', '.3gp', '.avi', '.mp3', '.m4a', '.wav', '.aac',
                        '.gif', '.bmp', '.webp', '.webm', '.mkv', '.tiff'}
    DB_EXTENSIONS = {'.db', '.sqlite', '.sqlite3', '.sqlitedb'}

    try:
        with zipfile.ZipFile(ufdr_path, 'r') as zf:
            zf.extractall(output_dir)

            for name in zf.namelist():
                full_path = os.path.join(output_dir, name)
                if not os.path.isfile(full_path):
                    continue

                result['total_files'] += 1
                ext = Path(name).suffix.lower()
                name_lower = name.lower()

                if ext in ('.html', '.htm'):
                    result['html_reports'].append(full_path)
                elif ext == '.csv':
                    result['csv_files'].append(full_path)
                elif ext in MEDIA_EXTENSIONS:
                    result['media_files'].append(full_path)
                elif ext in DB_EXTENSIONS or 'sqlite' in name_lower:
                    result['databases'].append(full_path)
                    result['sqlite_recovery_needed'] = True
                elif name_lower.endswith('-wal') or name_lower.endswith('-journal'):
                    # WAL and journal files — critical for recovery
                    result['databases'].append(full_path)
                    result['sqlite_recovery_needed'] = True
                else:
                    result['other_files'].append(full_path)

        # Summary for the analyst
        result['summary'] = (
            f"UFDR extracted: {result['total_files']} files to {output_dir}\n"
            f"  HTML reports: {len(result['html_reports'])}\n"
            f"  CSV files: {len(result['csv_files'])}\n"
            f"  Media files: {len(result['media_files'])}\n"
            f"  Databases: {len(result['databases'])}\n"
            f"  Other: {len(result['other_files'])}"
        )

        if result['sqlite_recovery_needed']:
            result['summary'] += (
                "\n  ⚠️  SQLite databases found — HAND OFF to dw-sqlite-recovery "
                "for WAL analysis BEFORE repeated file access"
            )

    except zipfile.BadZipFile:
        result['error'] = f"File is not a valid ZIP/UFDR: {ufdr_path}"
    except Exception as e:
        result['error'] = f"Extraction failed: {str(e)}"

    return result
