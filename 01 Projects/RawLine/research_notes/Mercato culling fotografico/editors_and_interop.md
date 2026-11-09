# Photo editors/DAMs: culling features and how a standalone culling app must interoperate with them (state as of Nov 2026)

Scope: Lightroom Classic (LrC), Lightroom cloud/desktop, Capture One, DxO PhotoLab, ON1 Photo RAW, darktable, Apple Photos, Adobe Bridge. Also reference culling apps (Photo Mechanic, FastRawViewer, Narrative) and per-format quirks (ARW, CR3, NEF, RAF, DNG, RAW+JPEG). This scope was extended mid-task to cover all camera brands.

Source quality: most interop detail comes from Adobe Community, Capture One community, the FastRawViewer and darktable manuals, and Camera Bits docs. Several primary pages were not reachable (Adobe HelpX, the Capture One support article and PetaPixel returned 403, and the ExifTool forum was down). Where a claim rests only on a search-result summary of a page, it is marked "(snippet)".

---

## 1. Does Lightroom Classic read and write pick/reject flags in XMP?

### Takeaway
Yes, since **LrC 13.2 (February 2024)**. Older notes, the spec's current line ("I flag di Lightroom non passano dall'XMP") and older FastRawViewer docs say otherwise, and they are now out of date. LrC writes flags as `xmpDM:pick` (-1 / 0 / 1) plus `xmpDM:good` (true / false). Flags then sync through XMP to Lightroom desktop/cloud. A known bug means LrC may not write the flag if `xmpDM:pick` is not already in the file and nothing else changed. Section 4.6 of the spec should be revised.

### Cited Findings
- Adobe's help page (snippet) says: "with LrC 13.2, flag states are now saved to XMP. Thus, they are now visible or available outside of the Lightroom Classic catalog." — [Adobe HelpX: Flag, label, rate photos](https://helpx.adobe.com/lightroom-classic/help/flag-label-rate-photos.html)
- The LrC 13.2 release notes list "Support to read and write flag states to XMP". Community Expert Ian Lyons says this gives inter-app support for Pick and Reject flags. Flags saved to XMP (as a sidecar or embedded in DNG) are available to Lightroom desktop when files sync to the cloud, and the reverse also holds. Flags are global, not per collection. — [Adobe Community: LrC v13.2 and flags in XMP](https://community.adobe.com/t5/lightroom-classic-discussions/lrc-v13-2-and-flags-in-xmp/m-p/14440118)
- According to the ExifTool forum (snippet; the forum was offline when fetched), LrC 13.2 reads and writes two new fields: `xmpDM:pick` ("-1", "0", "1") and `xmpDM:good` ("true"/"false"). At the time, the Adobe XMP namespace docs specified only `xmpDM:good`. — [ExifTool forum: New Adobe Lightroom XMP fields](https://exiftool.org/forum/index.php?msg=85176)
- In a user test, `exiftool -xmp:pick` returned `Pick : 1` for a flagged photo and `Pick : 0` after unflagging. — [Adobe Community bug: Flag not saved to XMP if XMP:Pick missing](https://community.adobe.com/t5/lightroom-classic-bugs/flag-not-saved-to-xmp-if-xmp-pick-missing-from-file-metadata/idi-p/14479660)
- **Bug:** LrC 13.2 "won't save the current flag to XMP if the field XMP:Pick is missing from the file and no other metadata field has been changed in the catalog". Adobe acknowledged it. The workaround is to change some other field, or to run Save Metadata manually. LrC has no built-in way to find photos whose flag was never written. — [Adobe Community bug report](https://community.adobe.com/t5/lightroom-classic-bugs/flag-not-saved-to-xmp-if-xmp-pick-missing-from-file-metadata/idi-p/14479660); [How to find photos that do not have flag written into XMP](https://community.adobe.com:443/t5/bug-lightroom-classic/how-to-find-photos-that-do-not-have-flag-written-into-xmp/idi-p/14436839)
- A related report says LrC erases the pick state that comes from photos favorited on iOS. — [Adobe Community](https://community.adobe.com/t5/lightroom-classic-discussions/lr-classic-erases-pick-state-generated-from-ios-favorited-photos/td-p/14446893)
- digiKam users asked in Sept 2024 for support of `xmpDM:pick` and `xmpDM:good`. This shows other tools are starting to adopt the fields. — [digikam-users mailing list](https://mail.kde.org/pipermail/digikam-users/2024-September/036505.html)
- A feature request asks Adobe Bridge to support the Lightroom pick flag in XMP, which implies Bridge does not read it yet. — [Adobe Community feature request](https://community.adobe.com/feature-requests-559/add-support-in-bridge-for-lightroom-pick-flag-in-xmp-1641312)
- **Workarounds from before 13.2 (historical):**
  - FastRawViewer said Lightroom's reject flag "is not exported to XMP and no way to pass this flag back to Lr via sidecar files". — [FastRawViewer node/196](https://fastrawviewer.com/node/196)
  - FRV instead offers a "Use XMP Reject rating" option, which writes rejects as `xmp:Rating = -1` (turned on automatically with the Bridge label style). — [FastRawViewer manual: XMP metadata](https://www.fastrawviewer.com/usermanual15/xmp-metadata)
  - In a FRV thread, a user reports that a Pick made in Lightroom cloud's "Local File" mode is stored as `xmpDM:good="True"`. The nearest FRV equivalent was a label "Good to Use". FRV does not overwrite Lightroom-specific flags already in XMP. — [FastRawViewer node/1226](https://www.fastrawviewer.com/node/1226)
- Narrative's documented handoff is ratings, color labels, tags, rotation and crops, written to an XMP sidecar for RAW/DNG/HEIC and embedded in JPEG. Keywords are not saved. After culling the user runs Read Metadata from File in LrC, with this warning: "Either one can overwrite newer work". — [Narrative help: Sync metadata safely between Lightroom Classic and Narrative](http://help.narrative.so/en/articles/7337388-sync-metadata-safely-between-lightroom-classic-and-narrative)

### Inferences
- RawLine Selects can now write P/X/U as `xmpDM:pick` 1/-1/0, plus `xmpDM:good` true/false for picks. LrC 13.2+ and Lightroom desktop should then pick them up. This needs verification on Andrea's own LrC exports (the spec's sample-file step), especially:
  - the exact `xmpDM:good` value written for reject and for unflagged;
  - whether "Read Metadata from File" actually imports `xmpDM:pick`. No source tested this explicitly.
- Keep an optional legacy reject mode (`xmp:Rating=-1`) for Bridge, FRV and older LrC. Some tools treat -1 as reject.
- Write `xmpDM:pick` explicitly, including 0, on every flag change. LrC's own bug (it skips writing when the field is absent) suggests that a missing field is handled less reliably than an explicit 0. This is an inference.

### Gaps
- No primary Adobe documentation found for the exact `xmpDM:good` semantics or for the precedence between `xmpDM:pick` and `xmpDM:good` (the ExifTool table was not reachable).
- Not confirmed whether the 13.2 "flag not saved" bug was fixed in LrC 14/15.
- Not confirmed whether Capture One, DxO, ON1 or darktable read `xmpDM:pick`. No source found. Assume they do not.

---

## 2. Color label name mapping (LR vs Capture One vs Photo Mechanic vs Bridge), and incompatibilities

### Takeaway
Color labels are not standardized. LrC writes `xmp:Label` as a **localized text string** that must match the active label set's name exactly. Capture One historically read only `photoshop:Urgency` (numeric) but later versions give the label name precedence. Photo Mechanic and FRV match by exact text. Pink/purple urgency numbers have varied across C1 versions. Lightroom 15 (Oct 2025) reportedly adds `xmp:LabelColor` alongside `xmp:Label`. The spec's profile approach is correct. Writing the name plus optional Urgency, and reading tolerantly, is the industry-standard workaround.

### Cited Findings
- Lightroom stores color labels in `xmp:Label` as a plain string ("you can write xmp:label=Churchill"). LR's defaults are Red, Yellow, Green, Blue, Purple. — [Lightroom Queen forum](https://www.lightroomqueen.com/community/threads/can-lightroom-import-color-label-in-xmp.2575/) (snippet); [Adobe Community: export LR color labels to JPEG metadata](https://community.adobe.com/t5/lightroom-classic-discussions/export-lightroom-color-labels-to-jpeg-metadata/m-p/8835954) (snippet)
- **New in Lightroom 2025.10 / LrC 15.0:** a new XMP field for color labels, `xmp:LabelColor`, is added alongside the existing `xmp:Label`. — [Lightroom Queen: What's new in Lightroom 2025.10](https://www.lightroomqueen.com/whats-new-in-lightroom-2025-10/)
  - Field name as summarized from the article. The spec mentions `photoshop:LabelColor`. The exact namespace prefix must be checked on a real LrC 15 sidecar.
- Localization: LR writes localized strings ("Grün", "Rot"). Capture One then did not recognize them because it "only uses the english spelling". One user found that LR still used the system language for labels after switching its UI to English. — [Capture One community: Color Labels via xmp from Lightroom, German spelling](https://support.captureone.com/hc/es/community/posts/360014591338-Color-Labels-via-xmp-from-Lightroom-German-spelling-unable-to-import); [FastRawViewer node/542: labels not conforming to language setting in LR CC 8.0](https://www.fastrawviewer.com/node/542)
- Capture One (C1) writes both a color name and `photoshop:Urgency`.
  - **Older C1:** read only Urgency, and would update `xmp:Label` but not read it.
  - **Later C1:** a FRV forum user found Phase One changed this so the label name takes precedence. Full interoperability came from C1 default label names, LR default names, and FRV "Custom" with translated names, with FRV's Urgency option turned off.
  - FRV's developers say the Urgency option is now mainly for old C1. C1 writes "None" for unset labels on English locales.
  - Sources: [FastRawViewer node/395](https://www.fastrawviewer.com/node/395); [FastRawViewer node/485](https://fastrawviewer.com/node/485)
- **C1 Urgency values (user-reported, version-dependent):**

  | Label | C1 8 report | C1 9.1.1 Windows |
  |---|---|---|
  | none | 0 | |
  | red | 1 | |
  | green | 2 | |
  | blue | 3 | |
  | pink | 5 (same as purple; user suggested 4) | 4 |
  | purple | 5 | 5 |
  | orange | 6 | |
  | yellow | 7 | |

  A bug in older C1 produced 5 for Pink and was fixed in 9.1 for Windows. Daminion used different Urgency numbers, so yellow arrived as the wrong label. — [Daminion forum: Capture One 8 color label](https://forum.daminion.net/topic/2666-capture-one-8-color-label/) (snippet); [Capture One community: Color Labels](https://support.captureone.com/hc/de/community/posts/360012425998-Color-Labels) (snippet)
- digiKam gives `xmp:Label` priority over `photoshop:Urgency` when both exist. — [KDE bug 405472](https://bugs.kde.org/show_bug.cgi?id=405472)
- An ExifTool command can convert `photoshop:Urgency` numbers to `xmp:Label` names in bulk. — [ExifTool forum: Transferring Label Metadata](https://exiftool.org/forum/index.php?msg=57125)
- **Photo Mechanic:**
  - LrC and C1 recognize PM color classes only if "the text label for each class must be exactly the same in each app". For non-English apps, the user must type the localized names into PM.
  - PM ships "Snapshots" (Preferences > General > lightning bolt) that preset label names per target app.
  - Source: [Camera Bits: Star Ratings & Color Classes between Software](https://docs.camerabits.com/en/support/solutions/articles/48000223643)
  - Lightroom users still report PM labels not matching after import. — [Adobe Community: Color label not matching when importing from PhotoMechanic](https://community.adobe.com/t5/lightroom-classic-discussions/color-label-not-matching-when-importing-from-photomechanic/td-p/15588039) (snippet)
- **Adobe Bridge** default label names differ from LR's: "Select, Second, Approved, Review, To Do". FRV offers four label styles (Bridge, LR color marks, LR Review Status, Custom), and choosing the Bridge style enables XMP reject = -1. — [FastRawViewer manual](https://www.fastrawviewer.com/usermanual15/xmp-metadata)
- Bridge and LrC label sets differ between versions. — [Adobe Community: labels in Br CC 2018 different from CS5/LrC 7.2](https://community.adobe.com/questions-558/labels-in-br-cc-2018-different-from-cs5-lr-classic-7-2-178991) (snippet)
- LR supports only 5 colors (Red, Yellow, Green, Blue, Purple). digiKam does not create or change `xmp:Label` for its orange, grey, black and white labels. — [KDE bug 412922](https://bugs.kde.org/show_bug.cgi?id=412922) (snippet)

### Inferences
- RawLine's profile system is the right design. Add these profiles:
  - **Capture One:** English names plus Urgency 1/7/2/3/5 for red/yellow/green/blue/purple. Urgency is off by default for modern C1 and on for "C1 legacy".
  - **Bridge:** Select / Second / Approved / Review / To Do, with -1 reject.
- When writing, also emit LrC 15's color field (`xmp:LabelColor`?) once its exact name and values have been confirmed from a real LrC 15 sidecar. This may eventually free us from localized label names.
- When reading, the precedence should be: (1) `xmp:Label` matched against all known names in all languages, (2) the new LabelColor field, (3) `photoshop:Urgency`.

### Gaps
- The exact namespace and value format of LrC 15's new `xmp:LabelColor` field were not verified. Adobe HelpX was not reachable.
- Current Capture One (16.x / 2025–2026) Urgency table and read precedence: no official doc reachable (the C1 support site returned 403).
- No official Camera Bits table of PM's XMP fields for color classes was found.

---

## 3. Sidecar naming and per-format quirks (ARW, CR3, NEF, RAF, DNG, JPEG/HEIF, RAW+JPEG; .cos, .acr, .dop)

### Takeaway
Adobe, Capture One, Photo Mechanic and FRV default to `basename.xmp` (`DSC0001.xmp`). darktable writes `basename.ext.xmp` (`DSC0001.ARW.xmp`) and also reads Adobe-style files. DNG, JPEG, TIFF, PSD and HEIC get XMP **embedded**, and LrC ignores sidecars for JPEGs. RAW+JPEG pairs with the same basename collide on one `.xmp`. Each app keeps its own private files: C1 `.cos` / `.cosession` / catalog DB, DxO `.dop`, ON1 `.on1`, darktable `.ext.xmp`. These do not conflict with Adobe's `.xmp` except darktable's, which is a different file. In-camera ratings vary by brand: Fuji RAF ratings are stored in MakerNotes and Canon video ratings in QuickTime:Rating, and LrC does not read either reliably.

### Cited Findings
- **FRV naming:** by default it searches `Filename.xmp`, then `Filename.XMP`, and creates `Filename.xmp`. A setting switches to `Filename.ext.XMP`. `xmp:MetadataDate` decides which copy wins when both an embedded block and a sidecar exist. — [FastRawViewer manual](https://www.fastrawviewer.com/usermanual15/xmp-metadata)
- **LrC and JPEG/import behavior (FRV manual):**
  - Lightroom ignores XMP sidecars for JPEGs, so XMP must be embedded in the JPEG.
  - LR ignores sidecars during card imports, so files should be copied to disk first.
  - For photos already in a catalog, use Metadata > Read Metadata from Files.
  - Source: [FastRawViewer manual](https://www.fastrawviewer.com/usermanual15/xmp-metadata)
- **darktable naming and import:**
  - darktable uses `<basename>.<extension>.xmp` and also looks for Lightroom's `<basename>.xmp` at import.
  - It loads tags, color labels, ratings and GPS from LR sidecars. It reads Lightroom-style files but never writes them.
  - It only partially converts LR develop settings.
  - Sources: [darktable manual: importing sidecar files generated by other applications](https://docs.darktable.org/usermanual/stable/en/overview/sidecar-files/sidecar-import/); [pixls.us: darktable and LR/FRV XMP](https://discuss.pixls.us/t/darktable-and-lr-fast-raw-viewer-xmp-files/5369/9)
  - darktable 3.8 did not read Bridge ratings because darktable writes the rating as an attribute of `rdf:Description`, while Bridge writes it as a child element. — [pixls.us thread](https://discuss.pixls.us/t/darktable-3-8-1-will-not-read-star-ratings-created-in-adobe-bridge-2022/30595)
- **RAW+JPEG collision:**
  - "If one shot raw + jpeg, and imported separately, the xmp filename maps to same, and saving xmp for one would overwrite the other."
  - Lightroom desktop deliberately adds a "-2" suffix when renaming mixed extensions to avoid the XMP name clash. Adobe staff called this "as per design".
  - LrC pairs RAW+JPEG by base name in the same folder. Unless "Treat JPEG files next to raw files as separate photos" is checked, the JPEG is treated as a sidecar of the raw.
  - LrC reads metadata from the .xmp (or the raw), "never from the JPEG".
  - Sources: [Adobe Community: LR Desktop 9.2 renaming adds suffix for mixed extensions](https://community.adobe.com/questions-680/p-lr-desktop-9-2-photo-renaming-adds-suffix-for-mixed-extensions-dng-jpg-1553606); [Adobe Community: RAW+JPEG, how does LR recognise pairs](https://community.adobe.com/t5/lightroom-classic-discussions/raw-jpeg-how-does-lr-recognise-images-that-belong-together/m-p/14503459/highlight/true) (snippet); [Adobe Community: LrC does not merge RAW and JPEG](https://community.adobe.com/t5/lightroom-classic-discussions/lr-classic-does-not-merge-raw-and-jpeg-while-importing/m-p/9915856) (snippet)
- **JPEG oddities:** LrC "Save metadata to file" sometimes writes huge `.acr` sidecars for JPEGs. Content-Credentials-signed JPEGs get an XMP file instead of embedded XMP. — [Adobe Community: .acr sidecars for JPEGs](https://community.adobe.com/bug-reports-674/p-save-metadata-to-file-sometimes-writes-huge-acr-sidecars-for-jpegs-unnecessarily-1555943/index2.html) (snippet); [Adobe Community: Content Credentials signed images create XMP for JPEG](https://community.adobe.com/t5/lightroom-classic-discussions/p-content-credentials-signed-images-will-create-an-xmp-file-for-jpeg-images/m-p/15080291/highlight/true) (snippet)
- **DNG:** flags saved to XMP "as sidecars or embedded in DNG" sync to LR desktop. — [Adobe Community: LrC 13.2 flags](https://community.adobe.com/t5/lightroom-classic-discussions/lrc-v13-2-and-flags-in-xmp/m-p/14440118)
- There is also a known case where LrC reads metadata for a DNG from an associated sidecar. — [Adobe Community: LrC reads metadata for a DNG from an associated sidecar](https://community.adobe.com/t5/lightroom-classic-discussions/p-lrc-reads-metadata-for-a-dng-from-an-associated-sidecar/m-p/13229135) (snippet)
- **Narrative's practice:** sidecar for RAW, DNG and HEIC; embedded for JPEG. — [Narrative help](http://help.narrative.so/en/articles/7337388-sync-metadata-safely-between-lightroom-classic-and-narrative)
  - Note: this differs from Adobe, which embeds XMP in DNG.
- **Capture One:**
  - Metadata lives in `.cos` files for sessions and in the database for catalogs.
  - "Auto Sync Sidecar XMP" (Preferences > Image) has three modes: Full Sync (two-way), Load (read only) and None (manual via Image > Sync Metadata).
  - Full Sync can be "a terrible slow-downer" on large catalogs.
  - C1 is "designed not to auto check XMP changes for performance reasons", so external edits need a manual reload or sync.
  - Turning off sync does not delete XMPs that already exist.
  - Sources: [Capture One support article 360002544898](https://support.captureone.com/hc/en-us/articles/360002544898) (snippet; 403 when fetched); [C1 community: Auto sync sidecar XMP does not work](https://support.captureone.com/hc/de/community/posts/360012221997-Auto-sync-sidecar-XMP-does-not-work) (snippet); [C1 community: Will Capture One XMP sidecars clobber existing ones?](https://support.captureone.com/hc/de/community/posts/360011850197-Will-Capture-One-xmp-side-car-files-clobber-existing-ones-from-other-product) (title only)
- **DxO PhotoLab:**
  - Since v5, PhotoLab reads ratings from `.xmp` rather than `.dop`.
  - DxO can prefer its own stored data over the XMP once that data exists.
  - Users of older versions said color labels from LR/PM were ignored.
  - Sources: [DxO support article 6640759778333](https://support.dxo.com/hc/en-us/articles/6640759778333) (snippet); [DxO forum: Prefers DxO XMP or embedded data](https://forum.dxo.com/t/prefers-dxo-xmp-or-embedded-data/7442) (snippet); [DxO forum: colour labels no longer read from Lightroom](https://forum.dxo.com/t/colour-labels-no-longer-successfully-read-from-lightroom/41381) (snippet)
- **In-camera ratings by brand:**
  - **Canon:**
    - LrC reads ratings from `EXIF:Rating` and `XMP:Rating`.
    - Canon R-series **video** ratings go in `QuickTime:Rating`, which LrC does not read.
    - Photo ratings reportedly work, but one R6 user reports stars lost on import.
    - With two cards, the camera writes the rating only to the primary card.
    - Sources: [Adobe Community: Canon R video ratings don't survive import](https://community.adobe.com/questions-675/rating-videos-on-camera-canon-r-stars-don-t-survive-import-to-lr-classic-976090) (snippet); [Adobe idea: support Canon R video ratings](https://community.adobe.com/t5/lightroom-classic-ideas/p-support-canon-r-series-camera-ratings-for-videos-today-they-are-photo-only/idi-p/14612587) (snippet)
    - A separate bug report covers many metadata fields in CR3 files not being imported. — [Adobe bug: many metadata fields in CR3 not imported](https://community.adobe.com/t5/camera-raw-bugs/p-many-metadata-fields-in-cr3-files-not-imported/idc-p/12667191) (snippet)
  - **Fujifilm:**
    - In-camera RAF star ratings are stored in binary MakerNotes, not in Rating.
    - LrC does not recognize RAF ratings from the GFX100RF, while JPG and HIF ratings import fine.
    - A third-party LrC plugin, `incamera-fuji-ratings`, exists to fix this.
    - Sources: [ExifTool forum: Reading Fujifilm RAF star rating](https://exiftool.org/forum/index.php?msg=46524) (snippet); [Adobe bug: in-camera ratings from GFX100RF not importing](https://community.adobe.com/bug-reports-679/p-in-camera-star-ratings-from-fujifilm-gfx100rf-not-importing-662280) (snippet); [incamera-fuji-ratings plugin](https://awesome.ecosyste.ms/projects/github.com%2Faldis-ameriks%2Fincamera-fuji-ratings)
  - Lightroom has no built-in way to give a default rating at import while keeping in-camera ratings (old 2014 answer). — [UniquePhoto Q&A](https://www.uniquephoto.com/community/qa/can-lightroom-assign-1-star-on-import-without-overwriting-in-camera-ratings)

### Inferences
- RawLine defaults:
  - Write `basename.xmp` for every proprietary raw format (ARW, CR2, CR3, NEF, NRW, RAF, ORF, RW2, PEF, 3FR, IIQ, and so on).
  - When reading, also detect `basename.EXT.xmp` (darktable, FRV option) and an uppercase `.XMP`.
  - Embed XMP into DNG, JPEG, HEIF and TIFF by default, because LrC ignores JPEG sidecars and embeds into DNG.
  - Offer an option to write a sidecar for DNG/HEIC instead, as Narrative does.
- For RAW+JPEG pairs, write one shared `basename.xmp` for the raw and **also** embed the same rating, label and flag into the JPEG. LrC reads the raw's XMP and never the JPEG's. Other apps import the JPEG separately.
- When an XMP already contains `crs:` develop settings (from LrC or ACR), RawLine must patch only `xmp:Rating`, `xmp:Label`, `xmpDM:pick`/`good` and `xmp:MetadataDate`. Bumping `xmp:MetadataDate` matters because FRV and LR use it to decide which copy wins.
- In-camera ratings: RawLine should read `EXIF:Rating`, `XMP:Rating`, Fuji MakerNotes rating and `QuickTime:Rating` (for video), and offer to "promote" them into the XMP sidecar. This would solve a real LrC pain point, especially for Fuji RAF and Canon video.

### Gaps
- Sony in-camera rating storage in ARW: newer bodies (A1 II, A9 III, A7 IV) support in-camera rating, but no source on how it is stored or whether LrC reads it.
- Nikon NEF in-camera rating behavior and Nikon/Fuji/Canon "protect" flags: no source found on whether LrC or C1 read the protect/lock attribute.
- The XMP specification text on sidecar naming was not fetched. The basename rule is supported only by community statements and app docs.
- ACR `.acr` sidecars appear only for non-raw files (JPEG) per the bug report. No conflict with raw `.xmp` was found.

---

## 4. Culling features and speed inside each editor (2025–2026)

### Takeaway
- **LrC 15.0 (Oct 2025)** added Early Access **Assisted Culling** (sharpness, subject and eyes criteria, Selects/Rejects groups with batch actions, available in Library and Import). It also added **Auto Stacking by visual similarity**. Both run locally and focus on portrait/event work. Fast browsing in LrC still depends on "Embedded & Sidecar" previews in Library, and stutter of about 0.7 s per image is still reported.
- **Capture One** has a Cull/Importer view with Face Focus (since 16.2) but no AI culling as of Sept 2025.
- Other editors' culling relies mostly on their browsers. No speed data was found for them.

### Cited Findings
- **LrC Assisted Culling:**
  - Uses AI to judge sharpness and group by visual similarity, sorting photos into Selects and Rejects with Batch Actions.
  - Available in Classic (also at Import) and Lightroom Desktop. Early Access, "designed mainly for large volumes of people photos".
  - Auto-Stacking puts the best-rated photo on top and is not limited to people.
  - A commenter reports bracketed exposures are not stacked together.
  - Source: [Lightroom Queen: What's new in Lightroom 2025.10](https://www.lightroomqueen.com/whats-new-in-lightroom-2025-10/)
  - Adobe's Early Access thread says it runs locally without internet and is included in the subscription. Users report inconsistent subject detection and "eyes closed" false positives on weddings and events. The feature got several updates, with a changelog dated April 2026 (not retrieved). — [Adobe Community: Early Access Assisted Culling (LrC)](https://community.adobe.com/questions-675/early-access-assisted-culling-lrclassic-983825) (snippet); [Adobe Community: Assisted Culling, Lightroom desktop](https://community.adobe.com/t5/lightroom-ecosystem-cloud-based-discussions/early-access-assisted-culling-lightroom-ecosystem-desktop/m-p/15592782) (snippet); [Adobe Design: behind the design of Assisted Culling](https://adobe.design/ideas/behind-the-design-assisted-culling-in-adobe-lightroom) (title only)
  - PetaPixel says these features are in LrC 15.0. — [PetaPixel, 3 Nov 2025](https://petapixel.com/2025/11/03/lightrooms-new-features-ai-culling-auto-dust-removal-color-variance-slider-and-more) (snippet; 403)
- **LrC preview speed:**
  - "Embedded & Sidecar" shows the camera JPEG right away. These previews are not color-managed and do not match LR rendering, and the first edit triggers a real preview.
  - Fuji and Olympus embedded previews are small. With RAW+JPG, LR uses the sidecar JPG.
  - "Replace Embedded Previews with Standard Previews at Idle Time" exists.
  - Choosing only Minimal or Embedded makes LR build Standard and 1:1 previews as you work, which "hinders performance".
  - Library is faster than Develop for culling because Develop uses a separate, slower preview cache.
  - Sources: [Have Camera Will Travel: LrC embedded previews](https://havecamerawilltravel.com/lightroom/lightroom-classic-new-embedded-previews/) (snippet); [Adobe HelpX: Optimize performance](https://helpx.adobe.com/au/lightroom-classic/desktop/technical-support/performance-guidelines/optimize-performance-lightroom.html) (snippet)
- **LrC lag reports:**
  - About 0.7 s per image change in Library on a high-end Mac (M2 Pro 16 GB).
  - Stutter because in-frame images load full previews while others keep embedded ones.
  - "Click on a preview, it takes ten seconds".
  - 4K monitor performance regression.
  - Sources: [Adobe Community: performance shifting image to image, M2 Pro](https://community.adobe.com/t5/lightroom-classic-discussions/performance-shifting-from-image-to-image-m2-pro-16gb-ram/td-p/14606483) (snippet); [Adobe Community: ten seconds to come to attention](https://community.adobe.com/questions-675/click-on-a-preview-it-takes-ten-seconds-to-come-to-attention-983451) (snippet); [Adobe Community: regression on 4K monitor](https://community.adobe.com/questions-675/performance-regression-browsing-images-on-4k-monitor-979511) (snippet)
  - LrC 15 bug fixes include a delay when checking images at 100%. — [Lightroom Queen](https://www.lightroomqueen.com/whats-new-in-lightroom-2025-10/)
- **LrC metadata-write reliability complaints:** "13.2 for Mac no longer automatically creates or saves to XMP", and "LrC 14.1 doesn't automatically save XMP metadata". — [Adobe Community 13.2](https://community.adobe.com/t5/lightroom-classic-discussions/lightroom-classic-13-2-for-mac-no-longer-automatically-creates-or-saves-to-xmp-files/m-p/14532627/highlight/true) (snippet); [Adobe Community 14.1](https://community.adobe.com/questions-675/lr-classic-14-1-doesn-t-automatically-save-xmp-metadata-980682) (snippet)
- **Capture One culling:**
  - Face Focus was added to Cull & Importer in v16.2.0 (C1 23).
  - Users argue face zoom "is not AI culling", and say grouping is "not (yet) close" to AI tools.
  - A Sept 17, 2025 feature request for out-of-focus face detection is "Awaiting review".
  - C1 16.6's AI work is retouching (blemish removal), not culling.
  - Sources: [C1 community: AI Culling](https://support.captureone.com/hc/es/community/posts/10705908543773-AI-Culling) (snippet); [Capture One ideas FR-I-2340](https://captureone.ideas.aha.io/ideas/FR-I-2340) (snippet); [alexonraw: C1 AI retouching](https://alexonraw.com/capture-one-ai-retouching-all-what-you-need-to-know/) (snippet)
- **ON1 Photo RAW 2026:** reads keywords and star ratings from XMP but "not markings" (Jan 2026 review). 2026.3 lets users rename color labels and promises faster performance. — [Digitec/Galaxus ON1 review](https://www.digitec.ch/en/page/on1-photo-raw-better-than-expected-41365) (snippet); [ON1 blog: Photo RAW 2026.3 update](https://on1.com/blog/on1-photo-raw-2026-3-update-faster-performance-workflow-improvements-ai-enhancements) (snippet)
- **Lightroom cloud/desktop:**
  - Flags, ratings and labels in XMP sync with LrC through the cloud since 13.2.
  - LR desktop has no "Read Metadata from File" menu, and Narrative says to refresh the photo instead.
  - A 2020 report says ratings were not imported with raw + XMP into LR CC (may be outdated).
  - Sources: [Adobe Community 13.2 flags](https://community.adobe.com/t5/lightroom-classic-discussions/lrc-v13-2-and-flags-in-xmp/m-p/14440118); [Narrative help](http://help.narrative.so/en/articles/7337388-sync-metadata-safely-between-lightroom-classic-and-narrative); [Adobe Community: bulk import XMP sidecars with raw](https://community.adobe.com/t5/lightroom-ecosystem-cloud-based-discussions/bulk-import-xmp-sidecars-with-raw/m-p/10420468/highlight/true) (snippet)
- **Apple Photos:**
  - Does not read XMP sidecars. The Nitro developer confirms this.
  - On macOS 15 Sequoia, Photos "does not import any metadata from image .xmp (in previous macOS it imported some)".
  - Embedding metadata in the file is the workaround.
  - Sources: [ExifTool forum msg 88985](https://exiftool.org/forum/index.php?msg=88985) (snippet); [Gentlemen Coders (Nitro) support](https://support.gentlemencoders.com/?p=139632) (snippet); [Apple Discussions: Photos XMP not used on import](https://discussions.apple.com/thread/252607726) (snippet)
  - Photomator needs a manual "Scan Photos for Rating and Flag Collections" and does not track external changes. — [Pixelmator support](https://support.pixelmator.com/faq-photomator/advanced-workflows/importing-flags-and-ratings-from-other-apps-into-photomator)
- **Adobe Bridge:** reads and writes XMP automatically, and its label names are Select/Second/Approved/Review/To Do. It apparently does not read the LR pick flag (feature request open). — [FastRawViewer manual](https://www.fastrawviewer.com/usermanual15/xmp-metadata); [Adobe feature request](https://community.adobe.com/feature-requests-559/add-support-in-bridge-for-lightroom-pick-flag-in-xmp-1641312)

### Inferences
- Speed pitch for RawLine: LrC's best case still needs an import plus embedded previews and shows about 0.7 s per image or stutter. A culling app that shows the embedded JPEG instantly before any import remains a clear advantage. LrC 15's Assisted Culling has narrowed the AI gap only for portrait and event work, not for outdoor or landscape.
- Apple Photos needs embedded metadata, or the "export to folder" path. A sidecar handoff will not work there.

### Gaps
- No measured preview-generation numbers for C1, DxO, ON1 or darktable culling were found.
- LrC Assisted Culling: it was not confirmed whether its Selects/Rejects write flags, stars or labels, or whether it has reached general availability (the April 2026 changelog was not retrieved).
- No primary source was found for Capture One 2025–2026 release notes on culling.

---

## 5. How culling apps integrate with editors (plugins, catalog writing, "open in", drag & drop)

### Takeaway
No major culling app writes the LrC catalog directly. The universal handoff is **XMP sidecar or embedded XMP, then LrC import (which reads XMP) or "Read Metadata from File" for photos already in the catalog**. Some add an LrC plugin for extras. Narrative ships a plugin (File > Plug-in Extras) and a "ship" step that imports only photos not already in the catalog. Capture One users must set Auto Sync to Load or Full Sync, or run Sync Metadata manually.

### Cited Findings
- **Narrative:**
  - Writes XMP, then the user runs Read Metadata from File, testing on one photo first.
  - Narrative ships only photos not yet in an LrC catalog.
  - Read Metadata can remove a shipped AI Preset, so the user restores the "(via Narrative)" snapshot.
  - Plugin: File > Plug-in Extras > Sync Snapshots.
  - On Windows, open the target catalog in Library before dragging photos in.
  - Source: [Narrative help](http://help.narrative.so/en/articles/7337388-sync-metadata-safely-between-lightroom-classic-and-narrative)
  - Users report that not all images transfer when shipping. — [Adobe Community: not all images importing from Narrative Select](https://community.adobe.com/questions-675/not-all-images-importing-from-narrative-select-973247) (snippet)
- **FastRawViewer:** relies on Read Metadata from Files and Save Metadata / auto-write in LrC. Copy files off the card before LR import, because LR ignores sidecars on card import. — [FastRawViewer manual](https://www.fastrawviewer.com/usermanual15/xmp-metadata)
- **Photo Mechanic:** XMP plus matching label names through Snapshots. — [Camera Bits](https://docs.camerabits.com/en/support/solutions/articles/48000223643)
  - A third-party guide describes the Photo Mechanic and Capture One sync workflow. — [Image Alchemist: Sync metadata between Photo Mechanic and Capture One](https://imagealchemist.net/sync-metadata-between-photo-mechanic-and-capture-one) (title only)
- **Imagen:** exports culling ratings as XMP. — [Imagen support: How do I review culling ratings exported as XMP?](https://support.imagen-ai.com/hc/en-us/articles/19610326337693-How-do-I-review-culling-ratings-exported-as-XMP) (title only)
- **Aftershoot:** no documentation was found on how it transfers flags. A competitor's blog says Aftershoot split into Select/Edit/Retouch products (marketing source). — [Imagen blog](https://imagen-ai.com/post/aftershoot-vs-narrative-select-vs-imagen/) (snippet)
- **Low-quality third-party source:** a 2026 "ShotSelect" guide claims the pick flag is written as `xmp:Label="Pick"` and that LrC does not read sidecars on import. Both conflict with the Adobe sources above, so the guide is not reliable. — [shotselect.pages.dev guide](https://shotselect.pages.dev/guides/xmp-sidecars)

### Inferences
- RawLine's plan is sound: write XMP, use "Open in LR/C1", export a list of filenames, and explain "Read Metadata from File" on first use.
- A later small LrC Lua plugin could automate Read Metadata on the filtered set and turn selections into a Collection. This mirrors Narrative.
- For C1, document "Auto Sync Sidecar XMP = Load" (one-way, fast) as the recommended setting, plus Image > Sync Metadata for photos already in a session.

### Gaps
- No technical documentation was found for Aftershoot or Excire on LrC catalog integration.
- No source found on whether any culling app writes `.lrcat` (SQLite) directly. None appear to, and it is probably risky.

---

## 6. What pros dislike about culling inside LR/C1 (summary)

### Takeaway
The main complaints:
- slow image-to-image navigation and preview stutter in LrC, even on M-series Macs;
- the need to import before culling;
- unreliable XMP auto-write (13.2 and 14.1 reports);
- the flag-not-written bug;
- AI culling scoped to portraits, with false positives;
- C1's lack of AI culling, and the slowness of Full Sync XMP.

### Cited Findings
- About 0.7 s per image change in Library, with stutter between full and embedded previews. — [Adobe Community M2 Pro thread](https://community.adobe.com/t5/lightroom-classic-discussions/performance-shifting-from-image-to-image-m2-pro-16gb-ram/td-p/14606483) (snippet)
- "Lightroom Classic no longer usable due to long long pauses"; "LrC sluggish and uses lots of CPU in the background". — [Adobe Community](https://community.adobe.com/questions-675/lightroom-classic-no-longer-usable-due-to-long-long-pauses-1628160) (title); [Adobe Community](https://community.adobe.com/questions-675/lrc-sluggish-and-uses-lots-of-cpu-in-the-background-1561885) (title)
- Slow performance on a 540k-image catalog. — [Adobe Community](https://community.adobe.com/t5/lightroom-classic-discussions/performance-slow-on-large-catalog-540k-images/td-p/14868732) (title)
- Using Assisted Culling at import risks formatting a card before every photo was imported. — [Lightroom Queen](https://www.lightroomqueen.com/whats-new-in-lightroom-2025-10/)
- Assisted Culling has false positives on weddings and events. — [Adobe Early Access thread](https://community.adobe.com/questions-675/early-access-assisted-culling-lrclassic-983825) (snippet)
- C1 Full Sync XMP is "a terrible slow-downer", and C1 has no AI culling. — [C1 community](https://support.captureone.com/hc/de/community/posts/360012221997-Auto-sync-sidecar-XMP-does-not-work) (snippet); [C1 AI Culling thread](https://support.captureone.com/hc/es/community/posts/10705908543773-AI-Culling) (snippet)

### Inferences
- RawLine's measurable speed targets (spec section 3) should be benchmarked directly against LrC's "about 0.7 s per image in Library" figure. This is the most concrete number found.

### Gaps
- No controlled benchmark (images per second, preview time per ARW) was found for LrC, C1 or Photo Mechanic in 2025–2026. Only anecdotes.
