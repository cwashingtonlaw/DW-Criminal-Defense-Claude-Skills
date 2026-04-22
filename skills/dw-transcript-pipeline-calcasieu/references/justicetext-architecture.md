# JusticeText Architecture & API Reference

Technical analysis of JusticeText's internal architecture, conducted March 2026. This reference documents the platform's auth, upload, and API patterns for potential future automation of the upload step.

## Authentication

JusticeText uses **AWS Cognito** for authentication. No separate API key exists.

- **User Pool**: `us-east-2_TLtG4Aic6`
- **Client ID**: `8f6udv8m6ue5nnvtag0rvb6i0`
- **Identity Pool**: `us-east-2:979c9357-f995-4847-846c-7efbef19d4b5`
- **Region**: `us-east-2`

Tokens are stored in `localStorage` under keys:
- `CognitoIdentityServiceProvider.<clientId>.<email>.idToken`
- `CognitoIdentityServiceProvider.<clientId>.<email>.accessToken`
- `CognitoIdentityServiceProvider.<clientId>.<email>.refreshToken`

## File Upload Mechanism

JusticeText uploads files **directly to S3** using the AWS SDK's `MultipartUploadCommand` and `UploadPartCommand`. The flow:

1. Browser authenticates via Cognito → receives temporary AWS credentials
2. Browser creates an S3 client (AWS SDK v3 bundled in the frontend)
3. Files are uploaded via S3 multipart upload to the initial upload bucket
4. Browser calls JusticeText's filesystem API to register the uploaded file in the workspace

### S3 Buckets

| Bucket | Purpose |
|--------|---------|
| `useruploadedav192848-jtdevelop` | Initial audio/video upload destination |
| `usermediafinal` | Processed/final media |
| `usermediaavstandardformat` | AV standard format conversion |
| `usermediathumbnail` | Video thumbnails |
| `usermediaclips` | Clips extracted from media |
| `usermedia-proprietary-format` | Proprietary format files (AV3, FTR, etc.) |
| `prod-jt-document-initial-upload` | Document/PDF initial upload |
| `prod-jt-image-initial-upload` | Image initial upload |
| `prod-jt-image-standard-format` | Processed images |

## API Services

| Service | Base URL | Purpose |
|---------|----------|---------|
| Transcribe Service | `https://jttranscribeservice.justicetextapi.com` | File management, transcription |
| Transcript Data Service | `https://transcriptdataservice-http-prod.justicetextapi.com` | Transcript data, export |
| Note Service | `https://noteservice-prod.justicetextapi.com` | Notes/annotations |
| Miranda AI Service | `https://mirandaai-prod.justicetextapi.com` | AI assistant features |
| Thumbnail CDN | `https://cdn-thumbnails.justicetextapi.com` | Signed thumbnail URLs |

## Filesystem API Endpoints

Discovered via JS bundle analysis (`jttranscribeservice.justicetextapi.com`):

- `POST /api/filesystem/directory` — List/manage directories
- `GET /api/filesystem/directory/fileNames` — Get file names in directory
- `GET /api/filesystem/file/metadata` — Get file metadata
- `POST /api/filesystem/createFolder` — Create folder
- `POST /api/filesystem/renameFileOrFolder` — Rename file or folder
- `GET /api/filesystem/folders/fileCount` — Get file count
- `POST /api/filesystem/trash` — Move to trash
- `POST /api/filesystem/structureEntry/` — Structure entry operations
- `GET /api/filesystem/userContent` — User content listing

## Transcript API Endpoints

Discovered via JS bundle analysis (`transcriptdataservice-http-prod.justicetextapi.com`):

- `GET /api/folder/summary/{folderId}` — Workspace summary
- `POST /api/carousel?folderId={folderId}` — File carousel/list
- `GET /api/getTranscript` — Get transcript content
- `POST /api/updateTranscript` — Update transcript
- `POST /api/upsertTranscript` — Create/update transcript
- `GET /api/transcriptsMetadata/:fileid` — Transcript metadata
- `POST /api/transcripts/snapshots` — Transcript snapshots
- `POST /api/search/transcripts` — Search across transcripts
- `GET /api/search/transcripts/count` — Search result count
- `POST /api/deleteTranscriptAndSnapshots` — Delete transcript
- `GET /api/checkFilePermission` — Check file permissions
- `GET /api/getSharedFiles` — List shared files
- `POST /api/file/shareLink` — Generate share link
- `GET /api/file/:resourceId/thumbnail/url` — Get thumbnail URL

## Upload Dialog Options

JusticeText's upload dialog ("Select files for upload") offers:

**Online sources** (OAuth integrations):
- Google Drive
- Dropbox
- Microsoft OneDrive
- Box
- Evidence.com
- URL (direct link)
- Clio

**Proprietary formats** (folder upload for specialized formats):
- AV3 Folder
- FTR Folder
- Cathexis Folder
- Courtsmart Folder

**Local upload**:
- Drag and drop zone (up to 200 files)
- "Select files" button (opens native macOS file picker)

## Chrome Extension File Upload Limitation

**The Claude in Chrome extension's `file_upload` tool is globally disabled.** Testing conducted March 2026 confirmed:

- `DOM.setFileInputFiles` returns `{"code":-32000,"message":"Not allowed"}` on ALL sites
- Tested paths: Google Drive Stream (FUSE), SMB NAS mount (`/Volumes/`), local Desktop (`~/Desktop/`)
- Tested sites: JusticeText, httpbin.org (blank test page)
- Conclusion: This is a Chrome extension-level restriction, not site-specific or filesystem-specific

## Future Automation Path

If/when the `file_upload` tool is enabled, OR if a standalone upload script is built:

1. **Extract Cognito ID token** from browser `localStorage`
2. **Exchange for AWS credentials** via Cognito Identity Pool (`GetCredentialsForIdentity`)
3. **Create S3 client** with temporary credentials, region `us-east-2`
4. **Multipart upload** each file to `useruploadedav192848-jtdevelop` bucket
5. **Call filesystem API** (`POST /api/filesystem/directory`) to register files in workspace

A Python script using `boto3` and `requests` could implement this entirely outside the browser. The Cognito token would need to be extracted from the browser session (or the user could log in via the script using their credentials, but that's less secure).