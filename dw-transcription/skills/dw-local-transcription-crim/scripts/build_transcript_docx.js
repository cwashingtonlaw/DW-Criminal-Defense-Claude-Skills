// Step 6b: render pages.json as a court-reporter .docx
//   node build_transcript_docx.js pages.json out.docx
// Front matter below is a WORKED TEMPLATE from a real transcript -- replace the
// caption, appearances, source table, methodology and annotations per matter.
// Spec: references/front-matter-spec.md   Annotations: assets/annotation-catalog.md
const fs = require('fs');
const d = require('docx');
const {
  Document, Packer, Paragraph, TextRun, PageBreak, AlignmentType, HeadingLevel,
  Header, Footer, PageNumber, NumberFormat, Table, TableRow, TableCell, WidthType, ShadingType,
  BorderStyle, TabStopType, VerticalAlign,
} = d;

const data = JSON.parse(fs.readFileSync(process.argv[2] || 'pages.json', 'utf8'));

const MONO = 'Courier New';
const SERIF = 'Times New Roman';

const wp = (text, opts = {}) => new Paragraph({
  alignment: opts.align || AlignmentType.LEFT,
  spacing: { before: opts.before ?? 0, after: opts.after ?? 100, line: opts.line, lineRule: opts.lineRule },
  indent: opts.indent,
  pageBreakBefore: opts.pageBreakBefore || false,
  border: opts.border,
  children: [new TextRun({
    text, font: opts.font || SERIF, size: opts.size || 22,
    bold: opts.bold || false, italics: opts.italics || false,
    allCaps: opts.caps || false, color: opts.color,
  })],
});

const rule = () => new Paragraph({
  spacing: { before: 60, after: 120 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: '000000' } },
  children: [new TextRun({ text: '', size: 2 })],
});

const h = (text) => wp(text, { bold: true, size: 24, before: 240, after: 120 });

// ---------- generic 2-col label/value table -------------------------------
function kvTable(rows, w1 = 2600, w2 = 7480) {
  return new Table({
    columnWidths: [w1, w2],
    width: { size: w1 + w2, type: WidthType.DXA },
    rows: rows.map(([k, v], i) => new TableRow({
      children: [
        new TableCell({
          width: { size: w1, type: WidthType.DXA },
          shading: { type: ShadingType.CLEAR, fill: 'F2F2F2' },
          margins: { top: 60, bottom: 60, left: 100, right: 100 },
          children: [wp(k, { bold: true, size: 20, after: 0 })],
        }),
        new TableCell({
          width: { size: w2, type: WidthType.DXA },
          margins: { top: 60, bottom: 60, left: 100, right: 100 },
          children: [wp(v, { size: 20, after: 0 })],
        }),
      ],
    })),
  });
}

function gridTable(header, rows, widths) {
  const mk = (txt, bold, fill) => new TableCell({
    width: { size: widths[0], type: WidthType.DXA },
    shading: fill ? { type: ShadingType.CLEAR, fill } : undefined,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: [wp(txt, { bold, size: 18, after: 0 })],
  });
  const row = (cells, bold, fill) => new TableRow({
    children: cells.map((c, i) => new TableCell({
      width: { size: widths[i], type: WidthType.DXA },
      shading: fill ? { type: ShadingType.CLEAR, fill } : undefined,
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      children: [wp(c, { bold, size: 18, after: 0 })],
    })),
  });
  return new Table({
    columnWidths: widths,
    width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    rows: [row(header, true, 'E6E6E6'), ...rows.map(r => row(r, false))],
  });
}

// =========================== FRONT MATTER =================================
const fm = [];

fm.push(wp('14th JUDICIAL DISTRICT COURT', { bold: true, align: AlignmentType.CENTER, size: 26, after: 0 }));
fm.push(wp('PARISH OF CALCASIEU', { bold: true, align: AlignmentType.CENTER, size: 26, after: 0 }));
fm.push(wp('STATE OF LOUISIANA', { bold: true, align: AlignmentType.CENTER, size: 26, after: 300 }));

fm.push(wp('STATE OF LOUISIANA', { align: AlignmentType.CENTER, size: 22, after: 0 }));
fm.push(wp('VERSUS', { align: AlignmentType.CENTER, size: 22, after: 0 }));
fm.push(wp('SHELTREN TEREL TUCKER', { bold: true, align: AlignmentType.CENTER, size: 22, after: 0 }));
fm.push(wp('DOCKET NO. 18143-24, DIVISION B', { align: AlignmentType.CENTER, size: 22, after: 300 }));
fm.push(rule());

fm.push(wp('TRANSCRIPT OF RECORDED INTERVIEW', { bold: true, align: AlignmentType.CENTER, size: 30, after: 60 }));
fm.push(wp('DESMOND DURRELL BROWN', { bold: true, align: AlignmentType.CENTER, size: 28, after: 60 }));
fm.push(wp('Taken August 20, 2024, at 1:23 p.m.', { align: AlignmentType.CENTER, size: 22, after: 0 }));
fm.push(wp('Lake Charles Police Department — Violent Crimes Trailer', { align: AlignmentType.CENTER, size: 22, after: 0 }));
fm.push(wp('LCPD Report No. 24-3787 — Double Homicide, 709 Bradley Street, Apt. B', { align: AlignmentType.CENTER, size: 22, after: 300 }));
fm.push(rule());

fm.push(wp('Evidence Item #39 · Prepared for the defense of Sheltren Terel Tucker', { align: AlignmentType.CENTER, size: 20, italics: true, after: 0 }));
fm.push(wp('Christopher Washington, Calcasieu Parish Public Defender’s Office', { align: AlignmentType.CENTER, size: 20, italics: true, after: 0 }));
fm.push(wp('Transcript prepared August 6, 2026', { align: AlignmentType.CENTER, size: 20, italics: true, after: 300 }));

fm.push(wp('THIS IS NOT A CERTIFIED COURT REPORTER’S TRANSCRIPT. It is a defense-prepared working transcript of a recorded law-enforcement interview, produced by machine speech recognition with attorney-directed review. It has no independent evidentiary standing and must be verified against the source recording before use in any filing, examination, or stipulation.',
  { size: 20, italics: true, align: AlignmentType.JUSTIFIED, after: 200 }));

fm.push(wp('THIS DOCUMENT CONTAINS PERSONALLY IDENTIFIABLE INFORMATION spoken on the recording, including a Social Security number, dates of birth, telephone numbers, a home address, and the names of minor children. Handle accordingly. If any portion is filed or served, redact per La. R.S. 46:1844(W) and the protective order referenced at Case Brain § 7 #14.',
  { size: 20, italics: true, align: AlignmentType.JUSTIFIED, after: 200 }));

// ---- Appearances
fm.push(new Paragraph({ children: [new PageBreak()] }));
fm.push(h('APPEARANCES / PERSONS PRESENT'));
fm.push(kvTable([
  ['Interviewee', 'DESMOND DURRELL BROWN (DOB 09/14/1985) — co-defendant of record in this matter; not charged as of the date of this interview'],
  ['Law enforcement', 'DETECTIVE RANDOLPH, Lake Charles Police Department, Violent Crimes (self-identified on the record at Runtime 00:00:22)'],
  ['Law enforcement', 'DETECTIVE GEORGE MILLER, Lake Charles Police Department (identified as present on the record at Runtime 00:00:22)'],
  ['Examiners', 'DET. RANDOLPH conducts the examination from 00:00:04 to 00:54:10 and again from 00:58:09 to the close. DET. MILLER conducts it from 00:54:10 to 00:57:47. Identified by cross-recording voiceprint analysis and confirmed by the attorney — see Annotation 2.'],
  ['Others present', 'None identified on the record. [ATTORNEY TO VERIFY against the video.]'],
  ['Counsel present', 'None. Mr. Brown was advised of rights and waived them on the record. See Annotations 3 and 4.'],
]));

fm.push(h('DESIGNATION CONVENTION'));
fm.push(wp('Two law-enforcement officers are identified on the record, and BOTH question the witness. They have been separated by voiceprint analysis across recordings (see Methodology and Annotation 2). This transcript uses the standard court-reporter examination convention, with the examining officer named at each changeover:',
  { size: 20, align: AlignmentType.JUSTIFIED }));
fm.push(kvTable([
  ['BY DET. ___:', 'Marks a change of examiner. Every "Q." that follows is by the named officer until the next such marker. Derived from speaker-embedding analysis at the block level, which is reliable; individual line-level attribution within a block was NOT attempted and should not be inferred.'],
  ['Q.', 'A question or statement by the examining officer named in the most recent "BY DET. ___:" marker.'],
  ['A.', 'An answer or statement by Desmond Durrell Brown.'],
  ['[INAUDIBLE]', 'Speech present on the recording that could not be resolved with confidence.'],
  ['[PHONETIC]', 'A proper noun rendered by sound; spelling is unverified.'],
  ['[SIC]', 'Rendered as spoken/as recognized; see the cross-referenced annotation.'],
  ['[ ]', 'Square-bracketed words inside a line are editorial insertions supplying an obviously elided word. They are NOT on the recording.'],
  ['(Runtime hh:mm:ss)', 'Elapsed time from the start of Segment 1, assuming the four segments run continuously. See Annotation 1.'],
]));

// ---- Source media
fm.push(new Paragraph({ children: [new PageBreak()] }));
fm.push(h('SOURCE MEDIA'));
fm.push(gridTable(
  ['File', 'Bytes', 'Duration', 'Status'],
  [
    ['#39 Interview Desomnd Brown 8.20.24.06-16-2026T21-43-40 PDT_1-00000.MTS', '2,124,349,440', '30:19.8', 'TRANSCRIBED — Segment 1'],
    ['#39 ... PDT_2-00001.MTS', '821,941,064', '11:45.8', 'TRANSCRIBED — Segment 2'],
    ['#39 ... PDT_3-00002.MTS', '845,507,114', '12:06.4', 'TRANSCRIBED — Segment 3'],
    ['#39 ... PDT_4-00003.MTS', '630,128,640', '09:01.6', 'TRANSCRIBED — Segment 4'],
    ['#39 ... 06-24-2026T05-31-53 PDT_4-00003.MTS', '630,128,640', '09:01.6', 'DUPLICATE of Segment 4 (identical size and duration) — not transcribed'],
    ['00000.MTS', '2,124,349,440', 'unknown', 'NOT TRANSCRIBED — Google Drive cloud-only placeholder; bytes not present on disk'],
    ['00001.MTS', '2,124,644,352', 'unknown', 'NOT TRANSCRIBED — Google Drive cloud-only placeholder; bytes not present on disk'],
    ['00002.MTS', '2,124,939,264', 'unknown', 'NOT TRANSCRIBED — Google Drive cloud-only placeholder; bytes not present on disk'],
  ],
  [4200, 1700, 1300, 2880]
));
fm.push(wp('Total transcribed runtime: 1:03:11. All four transcribed segments are AVCHD 1440×1080 @ 59.94i with AC-3 48 kHz stereo audio.', { size: 20, before: 120 }));

// ---- Methodology
fm.push(h('METHODOLOGY AND LIMITATIONS'));
[
  '1.  Audio was demultiplexed from each .MTS container with FFmpeg (no re-encoding of the video; audio decoded from AC-3 and written to 16 kHz mono FLAC). No filtering, noise reduction, gain, or normalization was applied.',
  '2.  Speech recognition was performed locally on attorney hardware using OpenAI Whisper large-v3 (MLX build) with word-level timestamps, temperature fallback 0.0–1.0, and conditioning on previous text DISABLED to suppress carry-over hallucination. No audio was uploaded to any third-party transcription service. No initial prompt or name list was supplied to the recognizer, so no proper noun in this transcript was suggested to the model.',
  '3.  Speaker diarization: a first attempt using Resemblyzer d-vector embeddings with agglomerative cosine clustering was run and REJECTED (best silhouette 0.348 across 2–5 clusters; cluster boundaries straddled speaker turns). It was replaced by pyannote.audio 4.0.7 (speaker-diarization-community-1) running on Apple MPS, which resolved three distinct voices in this recording and placed the third exclusively in the final segment. The four segments were measured and found acoustically identical (RMS within 0.008, level within 0.9 dB, spectral centroid within 100 Hz), ruling out a gain or codec artifact at the file boundary.',
  '3a. Identification of the second examiner was made from other recordings in the same case, not from this one. Evidence Item #38 (Interview of Robert Davis, 08/19/2024) opens by naming ONE officer — "myself, Detective Randolph" — yielding a clean Randolph voiceprint, which the attorney confirmed by listening on 08/06/2026. That voiceprint matches this recording at cosine +0.913 (segment 1) and +0.907 (segment 4). Evidence Item #139 (Interview of Johnta Monge, 09/03/2024) opens by naming exactly TWO officers, "Detective Randolph ... Detective George Miller"; with Randolph fixed, the remaining officer voiceprint is Miller, and it matches the second examiner in segment 4 of this recording at cosine +0.790, against +0.113 and +0.239 for the other two speakers present. The examiner blocks in this transcript follow from that analysis.',
  '4.  Attorney-directed review corrected recognition errors that are unambiguous from context (for example, a spelled surname recognized as "D-R-O-W-N" is rendered "B-R-O-W-N"; "Lac-Cassine" is rendered "Lacassine"; "Iowa way" is rendered "Iowa," reflecting the local pronunciation of Iowa, Louisiana). Where a correction would change legal meaning — in particular within the rights advisement — NO correction was made and the passage is flagged. See Annotations 3 and 4. Flagged passages within the rights advisement were re-decoded a second time under different settings; where the two passes disagreed, the disagreement is reported rather than resolved silently.',
  '5.  This transcript has not been verified against the video by a human listener. Every runtime cited here is machine-derived. Verify any passage before quoting it in a pleading or using it on examination.',
].forEach(t => fm.push(wp(t, { size: 20, align: AlignmentType.JUSTIFIED, indent: { left: 200, hanging: 200 } })));

// ---- Annotations
fm.push(new Paragraph({ children: [new PageBreak()] }));
fm.push(h('ANNOTATIONS — ITEMS REQUIRING ATTORNEY VERIFICATION'));
fm.push(gridTable(
  ['#', 'Runtime', 'Issue'],
  [
    ['1', 'Throughout', 'COVERAGE GAP. Only four of the eight files in this evidence folder were readable. The three 2024-dated originals (00000/00001/00002.MTS, 6.37 GB combined) are Google Drive cloud-only placeholders and could not be opened. At the bitrate of the readable files those three represent roughly 90 minutes of recording, against 63 minutes transcribed here. Whether the 2026 export is a complete, unaltered copy of the 2024 originals CANNOT be determined from this record. Make the originals available offline and re-run before treating this transcript as complete. Runtime continuity across the four segments is ASSUMED, not verified; there may be gaps at the segment joins. THE ARITHMETIC, WHICH IS THE POINT: the detective states on the recording that it begins at 1:23 p.m. and concludes it at 3:03 p.m. — ONE HOUR AND FORTY MINUTES on the record. Only 1:03:11 of media exists in this folder. Roughly 37 minutes of the stated interview is not accounted for by the files the defense has. Some of that is certainly recorder pauses (there is at least one break, at Annotation 8). The three inaccessible 2024 originals total 6,373,933,056 bytes, which at Segment 1\u2019s measured rate of 1,167,355 bytes per second computes to approximately 1:31:00 — about 28 minutes MORE than the 2026 export actually contains. That inference is arithmetic from file size at a constant bitrate, not measurement, and it should be treated as a lead rather than a fact. Verify it by making the three originals available offline and probing them directly.'],
    ['2', '00:54:10 / 00:58:09', 'SECOND EXAMINER IDENTIFIED. Det. George Miller — named as present at 00:00:22 and silent for the first 54 minutes — takes over the questioning at 00:54:10 and holds it to 00:57:47, opening with "This is a broad statement and it is a direct question, but would you have any reason to kill her?" Det. Randolph resumes at 00:58:09. The identification is by cross-recording voiceprint (Methodology 3a), anchored on Item #38, where Randolph is the only officer named and whose voice the attorney confirmed on 08/06/2026. Block-level attribution is reliable; do NOT attribute any individual line within a block without checking the video.'],
    ['3', '00:03:37', 'MIRANDA — APPOINTED COUNSEL PRONG. HIGHEST-PRIORITY VERIFICATION ITEM. Two independent decoding passes of this passage were run. Pass 1: "If you cannot afford a lawyer, we won’t be able to appoint or represent you for any questions if you wish." Pass 2 (greedy, temperature 0, separately windowed): "if you cannot afford a lawyer we won’t be appointed to represent you point question if you wish." BOTH passes produce a NEGATION where the standard advisement is affirmative — "one will be appointed to represent you before any questioning if you wish." No correction was applied. COUNTER-HYPOTHESIS, stated plainly: "one will be appointed" and "we won’t be appointed" are acoustically close under fast speech, and this recognizer demonstrably mishears this recording — it rendered "you have the right to remain silent" as "you have the right to remain solid" on BOTH passes. So a consistent machine negation is NOT proof the detective negated the right. It is a reason to put on headphones. If he did say it, the waiver is materially defective and the co-defendant’s statement is suppressible; if he did not, this dies here and costs nothing.'],
    ['4', '00:03:44', 'MIRANDA — CONTINUING-RIGHT PRONG. RESOLVED — NO ISSUE. The first decoding pass rendered this prong as an interrogative ("Are you deciding to exercise these rights and stop answering any questions...?"), which would have been significant, because an affirmative answer to that question reads as an invocation. A second decoding pass resolved it to the standard declarative form: "You decide any time to exercise these rights and stop answering any questions or making any statements. You understand that right?" The transcript reflects the second pass. This entry is retained so the reader knows the passage was examined and cleared, not overlooked.'],
    ['5', '00:04:07 / 00:04:34', 'The advisement time and the waiver time are both recited as 1:27 p.m. No executed rights-and-waiver form appears in the material reviewed for this transcript. Obtain it.'],
    ['6', '00:40:35', 'VEHICLES. Mr. Brown identifies only a 2019 white Cadillac Escalade (titled to Taronda) and a 2014 white Nissan Maxima. NO Toyota Camry is mentioned anywhere in this interview, and the detective did not ask about one. Compare the State’s theory that Brown’s Camry was the getaway vehicle and that Brown lied about it (D2 Bates 000073–000075, 000080).'],
    ['7', '00:39:56', 'DETECTIVE’S STATEMENT: "Like I said, I don’t think you had anything to do with this... That’s why I want to rule everybody out." Said to a man later indicted as a principal. Preserve.'],
    ['8', '00:40:23 / 00:41:21', 'CONSENT. Oral consent to search the phone is requested and given. No written consent form is executed on the recording. A break follows; Segment 2 ends and Segment 3 resumes mid-topic. What happened during the break is not on this record.'],
    ['9', '01:02:20', 'Rendered as: "We take your guns a long time ago." Implies a prior law-enforcement seizure of firearms from Mr. Brown predating 08/20/2024. Verify and, if so, obtain the report.'],
    ['10', '00:30:32 / 01:01:17', 'TIMELINE. Mr. Brown places Mr. Tucker at a Left Right Center dice party in the Terrace on SATURDAY NIGHT — that is, August 17, 2024 — arriving roughly 9:00–10:00 p.m. and leaving roughly midnight. Note that the autopsies give a date of death of 08/17/2024 while the indictment alleges "on or about" 08/18/2024 (Case Brain § 7 #13). Reconcile before relying on either date.'],
    ['11', 'Various', 'PROPER NOUNS RENDERED BY SOUND and not verified: Taronda / "Malboro"; Kodin Harper Rowland; Tanisha Riggs; Iselyn Malva; Kimball; Jordan Winston-Lagrange; Nikki; Kayla Street; Easy Mart. Note that "Jordan Winston-Lagrange" here may or may not be the "Jordan Turner" listed as Evidence Item 85.'],
    ['12', '00:02:05', 'A full Social Security number is spoken on the recording and transcribed here. Redact before any filing or service.'],
  ],
  [500, 1300, 8280]
));

// ---- Keywords / tags
fm.push(new Paragraph({ children: [new PageBreak()] }));
fm.push(h('TAGS'));
fm.push(wp('Custodial-Posture Interview  ·  Miranda Advisement on Record  ·  Co-Defendant Statement  ·  Consent to Search (Phone)  ·  Homicide  ·  LCPD Violent Crimes  ·  US English  ·  Single-Channel Room Audio  ·  AVCHD / 4 Segments  ·  Contains PII',
  { size: 20, after: 200 }));

fm.push(h('KEYWORDS (spoken-word frequency, 11,215 words)'));
fm.push(wp(data.keywords.map(k => `${k.word} ${k.n}`).join('   ·   '), { size: 20, font: SERIF, after: 200 }));

fm.push(h('NAMED PARTIES AND PLACES (spoken-word frequency)'));
fm.push(wp(data.names.map(k => `${k.word} ${k.n}`).join('   ·   '), { size: 20, font: SERIF, after: 200 }));

fm.push(h('TOPIC INDEX'));
fm.push(gridTable(
  ['Runtime', 'Topic'],
  [
    ['00:00:04', 'Recording opens; date, time, location, report number, officers present'],
    ['00:00:25', 'Identification of interviewee; name, spelling, DOB, Social Security number, address'],
    ['00:03:00', 'Rights advisement begins'],
    ['00:04:12', 'Waiver of rights; interview proceeds'],
    ['00:05:09', 'Relationship with Courtney Grogan; birth of the child; paternity'],
    ['00:08:48', 'Custody and visitation history; police called to the Bradley Street residence'],
    ['00:10:13', 'Child support order; amounts; garnishment'],
    ['00:12:47', 'Family court; retention of Lafayette counsel; the same attorney also used by Tucker'],
    ['00:17:32', 'Frequency of contact with the child; death of Mr. Brown’s brother'],
    ['00:20:41', 'Mr. Brown’s characterization of the decedent'],
    ['00:21:56', 'How Mr. Brown met Sheltren Tucker — the Chuck E. Cheese party and the phone call'],
    ['00:26:53', 'The meeting in Tucker’s truck; the relationship that followed'],
    ['00:28:09', 'Other men in the decedent’s life; the "Army guy"'],
    ['00:30:32', 'SATURDAY NIGHT — the Left Right Center party; Tucker’s arrival and departure'],
    ['00:35:33', 'How Mr. Brown learned of the deaths; the 9:58 a.m. call from Angelica Weldon'],
    ['00:39:56', '"I don’t think you had anything to do with this"; consent to search the phone; vehicles'],
    ['00:42:04', 'Whether the child called Tucker "dad"'],
    ['00:45:17', 'What Tucker told Mr. Brown about the men around his daughter'],
    ['00:49:29', '"I was told something different" — the detective presses for consistency'],
    ['00:52:10', 'Custody of the surviving children after the deaths'],
    ['00:54:10', 'Direct denial: "Would you have any reason to kill her?"'],
    ['00:56:16', '"They think that Tucker did it"'],
    ['00:58:00', 'Notifying Tucker of the death; his reaction'],
    ['00:59:39', 'Tucker’s vehicle and phone'],
    ['01:02:20', 'Firearms; conclusion of the recording at 3:03 p.m.'],
  ],
  [1300, 8780]
));

fm.push(h('RUNTIME → PAGE:LINE CONCORDANCE'));
fm.push(gridTable(
  ['Runtime', 'Page:Line', 'Runtime', 'Page:Line'],
  (() => {
    const rows = [];
    const t = data.tsindex;
    for (let i = 0; i < t.length; i += 2) {
      const a = t[i], b = t[i + 1];
      rows.push([a.ts, `${a.page}:${a.line}`, b ? b.ts : '', b ? `${b.page}:${b.line}` : '']);
    }
    return rows;
  })(),
  [2520, 2520, 2520, 2520]
));

// =========================== BODY =========================================
const body = [];
data.pages.forEach((pg, pi) => {
  pg.forEach((line, li) => {
    const num = String(li + 1).padStart(2, ' ');
    body.push(new Paragraph({
      pageBreakBefore: (li === 0 && pi > 0),
      spacing: { before: 0, after: 0, line: 520, lineRule: 'exact' },
      children: [new TextRun({ text: `${num}   ${line}`, font: MONO, size: 24 })],
    }));
  });
});

// =========================== DOCUMENT =====================================
const wpHeader = new Header({
  children: [
    wp('ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL', { align: AlignmentType.CENTER, size: 18, bold: true, after: 0 }),
    wp('PREPARED IN ANTICIPATION OF LITIGATION', { align: AlignmentType.CENTER, size: 18, bold: true, after: 40 }),
  ],
});

const mkFooter = (label) => new Footer({
  children: [new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 40 },
    children: [new TextRun({
      text: `${label}  |  Desmond Durrell Brown — 08/20/2024 — LCPD 24-3787  |  Page `,
      font: SERIF, size: 16,
    }), new TextRun({ children: [PageNumber.CURRENT], font: SERIF, size: 16 })],
  })],
});

const doc = new Document({
  creator: 'Daniels & Washington / Calcasieu PDO',
  title: 'Transcript of Recorded Interview — Desmond Durrell Brown — 08/20/2024',
  description: 'Defense working transcript, State v. Sheltren Terel Tucker, No. 18143-24, 14th JDC Calcasieu',
  sections: [
    {
      properties: {
        page: { size: { width: 12240, height: 15840 }, margin: { top: 1260, bottom: 1080, left: 1440, right: 1440 },
                 pageNumbers: { start: 1, formatType: NumberFormat.LOWER_ROMAN } },
      },
      headers: { default: wpHeader },
      footers: { default: mkFooter('FRONT MATTER') },
      children: fm,
    },
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1260, bottom: 1080, left: 1080, right: 1080 },
          pageNumbers: { start: 1 },
        },
      },
      headers: { default: wpHeader },
      footers: { default: mkFooter('TRANSCRIPT') },
      children: body,
    },
  ],
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync(process.argv[3] || 'transcript.docx', b);
  console.log('wrote', b.length, 'bytes;', data.npages, 'transcript pages');
});
