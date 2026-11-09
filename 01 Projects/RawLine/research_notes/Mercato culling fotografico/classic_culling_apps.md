# Classic / speed-first culling and RAW-viewing apps on macOS (state at November 2026)

Research date: 8 November 2026. Scope: non-AI or speed-first tools (AI-first tools like Aftershoot, FilterPixel, Narrative are covered elsewhere). Goes beyond spec sections 1, 10, 12 of "RawLine Selects.md". Tool-call budget was limited (~20 calls); several items marked as Gaps need a follow-up pass. Several vendor pages (PetaPixel, Fred Miranda, Camera Bits release-notes path) returned 403/404 to the fetcher, so some claims rely on search-result snippets and are flagged.

## Q1. What makes Photo Mechanic the standard, and what do users dislike?

### Takeaway
Photo Mechanic (PM) is still the reference for speed-from-embedded-preview, folder-based (no import) culling and pro IPTC/ingest workflows; its 2026 development is focused on workflow plumbing (shortcuts, upload, new read formats) rather than culling innovation. Main dislikes: the late-2023 shift to subscription, high perpetual price with only one year of updates, dated UI, and macOS responsiveness issues already logged in spec section 10.

### Cited Findings
- **Latest build:** Photo Mechanic 2026.6, Build 9175, published 18 June 2026. It adds custom shortcuts for Upload templates, snapshots and the IPTC Metadata Info dialog; an option to hide the upload progress dialog; variables in SmugMug upload paths; **read-only AVIF and JPEG XL support**; and better selection of external editors on macOS. Fixes are listed only in the installer README or the forum post — [Camera Bits blog](https://home.camerabits.com/photo-mechanic-update-with-new-custom-keyboard-shortcuts-avif-support-and-more/)
- The same post links an article on the **end of Intel Mac support** (not read in detail) — [Camera Bits blog](https://home.camerabits.com/photo-mechanic-update-with-new-custom-keyboard-shortcuts-avif-support-and-more/)
- Updates go only to active subscribers and to perpetual holders still inside their maintenance window — [Camera Bits blog](https://home.camerabits.com/photo-mechanic-update-with-new-custom-keyboard-shortcuts-avif-support-and-more/)
- **Customizable keyboard shortcuts** arrived first on macOS (2025), then on Windows in a later update — [Camera Bits](https://home.camerabits.com/update-to-photo-mechanic-customizable-keyboard-shortcuts-on-windows-and-more/)
- **Pricing (vendor support page, undated but matches 2026 third-party guides):**
  - PM standard: $14.99/month, $149/year, or $299 perpetual.
  - PM Plus (adds the catalog): $24.99/month, $249/year, or $399 perpetual.
  - Source: [Camera Bits support](https://docs.camerabits.com/support/solutions/articles/48001252734-photo-mechanic-pricing-and-information). This settles the "$249–299, sources disagree" note in spec section 1: $249 is Plus annual, $299 is standard perpetual.
- Perpetual licenses include one year of updates — [unanswered.io 2026 guide](https://unanswered.io/guide/is-photo-mechanic-worth-the-money) (third party). Camera Bits extended free updates for some perpetual licenses bought between 11 March 2024 and 17 March 2025 — [Camera Bits](https://home.camerabits.com/announcing-extension-of-free-updates-for-some-perpetual-licenses/)
- **Subscription change (November 2023):** older perpetual licenses keep working as long as the OS allows, with no guarantee on new machines or OS versions — [PetaPixel, Nov 2023](https://petapixel.com/2023/11/15/photo-mechanic-caves-to-industry-trends-shifts-to-subscription-model) (search snippet only; the page returned 403). Licensing-change announcement — [Camera Bits](https://home.camerabits.com/changes-coming-to-photo-mechanic/)
- **User sentiment:** forum threads on the subscription and price, e.g. "Photo Mechanic has won :-(" on TalkPhotography and a Fred Miranda thread — [TalkPhotography](https://www.talkphotography.co.uk/posts/9725384/), [Fred Miranda](https://www.fredmiranda.com/forum/topic/1944002/) (Fred Miranda returned 403, so I could not read the content). A 2024 personal blog on returning to PM — [baty.net](https://baty.net/2024/06/photo-mechanic-2024)
- Third-party comparison credits PM's speed to rendering the embedded JPEG instead of decoding the RAW — [FilterPixel comparison](https://filterpixel.com/best-ai-photo-culling-software) (competitor-authored)
- **AF point display in PM:** the 2026.6 notes do not mention it. The other features in this list rest on the fetched release notes only.

### Inferences
- PM's moat is ecosystem (IPTC templates, code replacements, ingest, FTP/SmugMug upload, wire-service workflows), not culling UX. The 2025–2026 releases deepen that moat (upload shortcuts, SmugMug variables) and ignore AF point, burst grouping and AI. That leaves an opening for culling-only differentiation.
- Price anchor for RawLine: at $149/year or $299 perpetual, a free or one-time-price culler with AF point and synced compare undercuts PM on the culling job alone.
- The Intel deprecation means PM is now Apple-silicon-focused, like RawLine.

### Gaps
- Full 2026.6 fix list and any 2026.7+ build after June 2026 were not found (release-notes URL 404).
- Plus catalog specifics, plus user complaints about the catalog, were not verified this session.
- Whether PM 6 / 2026 shows Sony AF points: no source either way. Spec section 1 says "not found", which still stands.
- No independent speed benchmark of PM vs others was found.

## Q2. FastRawViewer: how it shows "real RAW", and is that valued?

### Takeaway
FastRawViewer (FRV) is the only mainstream tool built around the RAW data itself: RAW histogram, over/under-exposure overlays computed from RAW values, focus peaking, and 2/4-up multi-window. It is cheap ($23.99 one-time) and cross-platform. The developers explicitly refuse to show AF points, arguing they are unreliable in metadata.

### Cited Findings
- Current download version: 2.0.11.2088 (from installer file names; release date not shown). Price $23.99, one key covers 2 computers on Mac and Windows, 30-day trial. Runs on macOS 10.13+ and Windows 7–11 (64-bit) — [fastrawviewer.com](https://www.fastrawviewer.com/)
- The RAW histogram and OE/UE (over/under-exposure) indication come from the RAW data, not the embedded JPEG. Focus peaking highlights in-focus edges. Multi-window mode shows 2 or 4 images — [fastrawviewer.com](https://www.fastrawviewer.com/)
- Claims support for 1,316 cameras ("almost every single RAW format"); Sigma Foveon is excluded — [fastrawviewer.com](https://www.fastrawviewer.com/)
- Writes ratings, labels, titles and descriptions to XMP sidecars that converters read — [fastrawviewer.com](https://www.fastrawviewer.com/)
- **AF point:** the developers say focus points are not part of the raw data and must be "guessed" from makernotes. They decline to display them because they cannot verify every mode, camera and firmware, and think it may mislead. Users have requested this repeatedly — [FRV forum: Please show selected focus point](https://www.fastrawviewer.com/node/591), [Feature request: focus point display](https://www.fastrawviewer.com/node/1251), [Focus point for culling sharpness](https://www.fastrawviewer.com/node/826), [Zoom to focussed area?](https://fastrawviewer.com/node/872)

### Inferences
- The recurring forum requests show users want AF point plus zoom-to-AF even in the "technical" camp. FRV's refusal is a stance, not a technical impossibility; Sony's own Imaging Edge does it for the A1 (see Q3).
- "Real RAW" exposure checks are valued by a niche (landscape, ETTR shooters). For event and outdoor culling, the decisive features are speed plus focus checking. A RAW-based highlight-clipping overlay is a cheap differentiator for RawLine (computed off-thread only on demand).

### Gaps
- FRV release date for 2.0.11, and any 2026 roadmap, not found.
- Whether FRV multi-window zoom is synced: not confirmed on the homepage (spec section 1 states it is; not re-verified here).

## Q3. Which apps show the Sony AF point, focus peaking, eye/face zoom?

### Takeaway
Sony AF point overlays are rare. The confirmed ones are:
- Sony Imaging Edge Desktop (A1 and A7S III named, 2025)
- ApolloOne (AF points, but Sony per-model support unclear)
- Camera RawX (Quick Look extension, Sony listed)
- digiKam (Sony via a 2024 bug fix; brand coverage still growing in 8.8)
- some new indie apps

PM and FRV do not show it. Face zoom (Palomino: V key, largest face at 300%) and a focus score (ApolloOne Max) are appearing in the 2025–2026 newcomers.

### Cited Findings
- **Sony Imaging Edge Desktop (Viewer):** a 2025 update displays the focus frames used during shooting; the note names ILCE-7SM3 and **ILCE-1 (A1)** — [Sony Imaging Edge support](https://support.d-imaging.sony.co.jp/app/imagingedge/en/index.php)
- **ApolloOne (Mac App Store):**
  - Version 5.1.0 (22 Oct, year inferred as 2025 from the 5.0.0 30 Sep release). Requires macOS 14+.
  - Shows camera AF points (Standard edition and up). Per the App Store listing, it can also "magnify and cycle through AF points".
  - Focus Score grades sharpness 1–100, including on detected faces (Max edition).
  - Split View with synced zoom and scroll. Stacks, AI Rating and AI Keywords arrived in 5.0.0.
  - Video playback with frame-by-frame stepping.
  - Pricing: Standard $35.99 perpetual or $14.99/year; Pro $59.99 or $23.99/year; Max $99.99 perpetual.
  - Source: [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12)
  - The 3.8.0 notes mention AF support for the Nikon Z5 II; 4.1.0 added RawBridge for the Sony A7V (lossless ARW only) — [search snippets of App Store listing](https://apps.apple.com/gb/app/apolloone-photo-video-viewer/id1044484672)
  - Background on the developer — [PetaPixel Nov 2025](https://petapixel.com/2025/11/14/how-two-photographers-transformed-raw-photo-support-on-mac), [DPReview forum: ApolloOne v4 and Camera RawX v2](https://www.dpreview.com/forums/threads/apolloone-v4-and-camera-rawx-v2.4815583)
- **Camera RawX** (same developer, Quick Look extension): "Show AF Points overlay" inside Finder Quick Look; supports Canon, Fujifilm, Nikon, OM/Olympus and Sony — [App Store](https://apps.apple.com/us/app/camera-rawx/id6587554858)
- **digiKam:**
  - Bug 490330 reported that focus points were not displayed for the Sony a6700 (JPG/HEIF/ARW) — [KDE bugs](https://bugs.kde.org/show_bug.cgi?id=490330). A search summary states Sony support landed in 8.5.0, but I did not verify this in the bug thread.
  - 8.8.0 (October 2025) extended focus-point display (Olympus/OM confirmed; a user reports RAF works). Pentax followed in a November 2025 thread — [digikam-users Oct 2025](https://mail.kde.org/pipermail/digikam-users/2025-October/037768.html), [Nov 2025 thread](https://mail.kde.org/pipermail/digikam-users/2025-November/037824.html)
- **FastRawViewer:** has focus peaking but no AF point (see Q2) — [fastrawviewer.com](https://www.fastrawviewer.com/)
- **Palomino:** V key zooms to the largest face at 300%, with a blink badge. No AF point mentioned — [palomino-app.com](https://palomino-app.com/)
- **RawCull (two different sites):** the rawcull.netlify.app docs (search snippet) say it currently supports only Sony A1 Mk I/II ARW. Spec section 1 says RawCull overlays the Sony AF point via ExifTool — [RawCull docs](https://rawcull.netlify.app/_print/docs/). By contrast, rawcull.com lists 10 brands, needs dcraw via Homebrew, and does not mention AF point — [rawcull.com](https://rawcull.com/). **Possible name clash between two products; verify.**

### Inferences
- Sony's own viewer proves the A1 focus-frame data is decodable and reliable enough for Sony to ship. That undercuts FRV's "unreliable" argument at least for the A1. RawLine can cite Imaging Edge as parity, but with a fast culling UX Imaging Edge lacks.
- ApolloOne is the closest established Mac competitor to RawLine's "AF point + zoom from there" pitch: it has AF point cycling, synced split view, stacks and focus score. It deserves a hands-on test with A1 ARW files.

### Gaps
- Whether ApolloOne shows AF points for the **Sony A1** specifically (vs. Nikon/others) is not confirmed.
- Eye-zoom behavior in Bridge, XnView MP and Raw Power was not researched.
- Whether PM or FRV have eye/face zoom: no source.

## Q4. Synced zoom compare, burst stacking, auto-advance: who has what

### Takeaway
Synced compare is now common:
- ApolloOne (Split View)
- OptiCull (side-by-side, synced zoom)
- FRV (2/4-up)
- Palomino (C key, reference frame)

Burst grouping with a sharpness pick has spread from AI tools to cheap indie apps (Palomino crown, ApolloOne Stacks/Focus Score). PM's long-standing strengths remain auto-advance and folder/card-based work, not bursts.

### Cited Findings
- **Palomino:**
  - Shortcuts: 1–5 stars, 6–9 color labels (red/yellow/green/blue), P pick, X reject. Labels and ratings go to standard XMP sidecars.
  - C compares two frames with one held as reference (synced zoom not described).
  - Bursts are grouped and ranked by sharpness, with a crown on the suggested best; "reject others" rejects the rest.
  - Reads the embedded JPEG ("10–100× faster", vendor claim) and prefetches the next photo. A session summary shows photos per minute.
  - Free with a 50-export cap per session; Pro is $29.99 one-time (Mac App Store). macOS 15+. Formats include ARW, DNG, 3FR, NEF, CR3, RAF, ORF and HEIC.
  - Source: [palomino-app.com](https://palomino-app.com/)
- **ApolloOne:** Split View with synced zoom and scroll; Stacks (5.0.0) — [App Store](https://apps.apple.com/us/app/apolloone-photo-video-viewer/id1044484672?mt=12)
- **OptiCull** (Mac App Store, Dope AI): free manual culling and ratings, side-by-side with synced zoom. While copying, it renames, analyzes and builds previews from RAW data in memory — [App Store](https://apps.apple.com/us/app/opticull-fast-photo-culling/id6448657895?mt=12), [dopeai.tech](https://dopeai.tech/opticull), [PetaPixel 2023](https://petapixel.com/2023/06/07/opticull-uses-ai-to-assess-sort-and-rate-your-photos)
- **Photo Mechanic:** auto-advance and tagging are documented in spec section 12. No burst grouping is mentioned in the 2026.6 notes — [Camera Bits](https://home.camerabits.com/photo-mechanic-update-with-new-custom-keyboard-shortcuts-avif-support-and-more/)

### Inferences
- Burst grouping plus a sharpness suggestion is becoming table stakes even in $30 apps, so RawLine must ship it in 1.0. The differentiator is *measuring sharpness at the Sony AF point*, which nobody advertises.

### Gaps
- Auto-advance support in Palomino, ApolloOne and OptiCull was not confirmed.
- Synced zoom in FRV, Bridge and XnView MP was not re-verified this session.

## Q5. Newcomers 2024–2026 and other viewers (XnView MP, digiKam, Bridge, Raw Power, FilterPass, PhotoSift)

### Takeaway
2025–2026 brought a wave of small native Mac culling apps:
- Palomino, PickShot, Phiewer Select and Photo Cull Pro, all requiring macOS 13–15+
- RawCull, culler, PhotoCuller, Fovea and unraw

They are almost all built around embedded-JPEG speed, XMP sidecars and one-time or low prices. "FilterPass" and "PhotoSift" could not be found as macOS culling products. The general-purpose viewers (XnView MP, digiKam) keep adding metadata depth but are not culling-focused.

### Cited Findings
- **Photo Cull Pro:**
  - Native app for macOS 15.6+. Claims RAW previews load in under 200 ms.
  - The paid tier adds XMP sidecar export for Lightroom and Finder color labels; $29/year or $79 lifetime.
  - Source: [App Store](https://apps.apple.com/app/id6757907514) (search snippet)
- **Phiewer Select** (macOS 15+): fast keep/reject with preloading and an optional RAW+JPG pairing mode — [App Store](https://apps.apple.com/app/id6766049040) (snippet)
- **PickShot** (macOS 13+): free culling viewer with optional AI culling, paid Pro tier and JPG+RAW pairing — [App Store](https://apps.apple.com/app/id6764620388) (snippet)
- **culler:** free, keyboard-driven, writes ratings and edits to XMP sidecars. Builds are not notarized, so Gatekeeper blocks the first launch — [culler releases](https://mertenssander.github.io/culler-releases/)
- **PhotoCuller:**
  - One-time purchase, fully offline, integrates with Apple Photos. Mac (Apple silicon, macOS 15+), iPad and iPhone.
  - Sources: [photoculler.com](https://photoculler.com/), [SLR Lounge review](https://www.slrlounge.com/photoculler-review-what-is-photoculler/)
- **Fovea:** AI culling plus a native RAW develop module; pre-groups bursts and highlights the sharpest eyes — [get-fovea.app](https://get-fovea.app/)
- **unraw:** paid Mac culling tool with RAW preview and Lightroom integration, from €99/year — [itechguides](https://www.itechguides.com/products/unraw/) (snippet)
- **PhotoSort:** Windows/Mac, JPG+RAW, moves files rather than deleting them — [AlternativeTo](https://alternativeto.net/software/photosort/about)
- **Cullstack** is listed as an alternative — [AlternativeTo](https://alternativeto.net/software/cullstack/about/) (details not read)
- **XnView MP:**
  - 1.9.x line through 2025–2026: 1.9.4 (September 2025) bundled ExifTool 13.37; 1.9.6 added full camera metadata via ExifTool including makernotes, Advanced Search with boolean operators, and Smart Albums. 1.9.8 and 1.9.9 releases exist.
  - A 1.9.1 bug: "Convert to series" altered photos without any action selected (fixed in 1.9.4).
  - Sources: [PortableApps](https://portableapps.com/node/79423), [XnView forum 1.9.6](https://newsgroup.xnview.com/viewtopic.php?p=210321), [Neowin 1.9.8](https://www.neowin.net/amp/xnview-mp-196/), [warp2search 1.9.9](https://www.warp2search.net/story/xnview-mp-199-released/), [XnView forum bug](https://newsgroup.xnview.com/viewtopic.php?p=209059)
- **digiKam:**
  - 8.6.0 (15 March 2025): face recognition overhaul and auto-tagging, 140 bug fixes — [digikam.org](https://digikam.org/news/2025-03-15-8.6.0_release_announcement)
  - 8.7.0 (mid-2025): AI auto-rotation plugin — [It's FOSS](https://news.itsfoss.com/digikam-8-7-release)
  - 8.8.0 (October 2025): more focus-point brands — [digikam-users](https://mail.kde.org/pipermail/digikam-users/2025-October/037768.html)
- **FilterPass:** no product found under this name. The closest matches are FilterPixel (AI culler, covered elsewhere) and FilterPro (an iOS preset editor, unrelated) — search results only.
- **PhotoSift:** no macOS culling product found. The searches surfaced other apps instead (Phiewer Select, Photo Cull Pro, PickShot and others).
- **CullAi** (2020, free AI culling for Mac) is older context — [PetaPixel 2020](https://petapixel.com/2020/12/11/cullai-is-a-free-artificial-intelligence-culling-tool-for-the-mac/), [Fstoppers](https://fstoppers.com/originals/cullai-mac-good-idea-has-way-go-538305)

### Inferences
- The indie newcomer pattern is the same as RawLine's plan: embedded JPEG, prefetch, XMP sidecar, one-time price, macOS 15+. Differentiation must come from Sony AF point accuracy, video in the same cull, label compatibility profiles, and stability, not raw speed alone.
- Many newcomers gate XMP export behind payment (Photo Cull Pro, Palomino's export cap, RawCull's export lock). A free beta with full XMP is a clear acquisition lever.

### Gaps
- **Not researched this session (budget):**
  - Adobe Bridge 2026 version and viewer features.
  - Raw Power (Gentlemen Coders) current status.
  - Picture Instruments tools.
  - qView.
  - Version and launch dates for the newcomers (most pages show no version or date).
- No independent measured benchmarks were found for any app. All speed claims (Palomino 10–100×, Photo Cull Pro <200 ms, RawCull "zero wait") are vendor claims.
- **Stability / bug reports** for the newcomers and for ApolloOne 5.x were not found.
- "FilterPass" and "PhotoSift": the coordinator should confirm the intended product names. PhotoSift may be the old Windows-only open-source image sorter; not verified.

## Q6. Multi-brand coverage (added at user request): RAW formats, per-format speed, per-brand gaps

### Takeaway
The hard multi-brand cases in 2026 are:
- **Nikon HE/HE\* NEF** (Z8, Z9, Zf, Z6 III): unsupported by LibRaw-based tools for years and by macOS until Tahoe 26.4.
- **Canon CR3 with HDR/HEIF previews**, which PM cannot preview.
- **Canon CRAW/lossy** (historically JPEG-preview-only in FRV).
- **Brand-uneven AF point display:** even Adobe's new overlay misses many Sony files.

Embedded-JPEG apps (PM, Palomino, PickShot and similar) are fast on every brand because speed does not depend on the codec. Brand gaps appear only when the app decodes RAW or parses makernotes (AF points). I found no per-format speed benchmarks for any app.

### Cited Findings
- **Photo Mechanic formats and metadata:**
  - Always shows the embedded JPEG ("fastest browsing experience"); rendering from RAW requires Adobe DNG Converter, which carries a speed cost.
  - **Embedded + sidecar XMP options:** ARW, CR2, ERF, NEF, NRW, ORF, PEF, RW2, SRF, STI.
  - **Sidecar only:** CR3, CRW, IIQ, MOS, RAF, SR2, X3F.
  - **DNG:** embedded only.
  - **Canon CR3 shot in HDR modes** embeds a HEIF that PM *cannot preview*; the workaround is recording an HEIF sidecar in camera.
  - **Video:** AVI, MOV, MPEG and MP4 are supported, with metadata in XMP sidecars only; playback is macOS-only.
  - Source: [Camera Bits supported formats](https://docs.camerabits.com/support/solutions/articles/48001252642-supported-file-formats)
- **PM and Nikon HE:** the PM docs do not address HE. One user report (DxO forum) says PM and DxO PL6 failed on recent Z9 files and claims "no one supports" HE NEFs on Apple silicon. This is unofficial and probably dated — [DxO forum](https://feedback.dxo.com/t/dxo-pl6-barfs-on-images-ingested-using-photo-mechanic-6/29747)
- **FastRawViewer per brand:**
  - **Nikon HE:** 2.0.9 added HE/HE\* support for the Z8, Z9, Zf and Z6 III, and the beta fixed an HE memory leak. Before that, 2.0.8 stated the Z8 HE/HE\* was unsupported, and a 2024 forum post said HE\* showed as JPEG preview only — [FRV 2.0.9 beta](https://www.fastrawviewer.com/blog/FastRawViewer-2-0-9-Beta), [FRV 2.0.9 release](https://www.fastrawviewer.com/comment/6186), [FRV Z9 thread](https://www.fastrawviewer.com/node/999), [version history](https://fastrawviewer.com/blog/releases/frv)
  - **Canon CR3:** supported since 1.5.1 (2019); CR3 roll/RAW burst added in 2.0.4; 2.0.9 improved damaged/modified CR3 handling — [FRV 1.5.1](https://www.fastrawviewer.com/node/573)
  - **Canon CRAW:** the 1D X III CRAW was JPEG-preview-only in 1.5.6 and got lossy support in 1.6.1 — [FRV 1.6.1](https://www.fastrawviewer.com/node/698)
  - Sigma Foveon RAW is not supported — [fastrawviewer.com](https://www.fastrawviewer.com/)
- **LibRaw dependency:** apps built on LibRaw (e.g. Tonfotos) could not read HE files because LibRaw lacked HE/HE\* — [Tonfotos community](https://community.tonfotos.com/d/1094-support-for-nef-files-when-high-efficiency-option-is-activated). Excire documents a similar Nikon HE limitation — [Excire KB](https://support.excire.com/portal/en/kb/articles/problems-with-certain-nikon-raw-formats-high-efficiency-compression)
- **macOS system RAW (ImageIO / Core Image), which matters for any native Swift app including RawLine:**
  - Z8/Z9 *lossless* NEF has been supported since around February 2024; Apple's RAW support page footnotes the Z8 as lossless-only — [Apple Community](https://discussions.apple.com/thread/255894628), [Apple Community JP 2025](https://discussions-jp-prz.apple.com/thread/255993381), [ZSystemUser 2024](https://www.zsystemuser.com/nikon-z-system-news-and/2024-newsviews/apple-updates-nef-support.html)
  - **macOS Tahoe 26.4 (March 2026)** reportedly began passing HE/HE\* through to apps like Photos, and Apple had not updated its public support page — [ZSystemUser](https://www.zsystemuser.com/accessories/versions-of-nikon-software.html). A BCG thread title says the same about thumbnails, but I could not read the content — [BCG Forums](https://bcgforums.com/goto/post?id=587961). Single secondary source; **verify on device**.
  - Sequoia 15.4 broke NEF display in Preview for some users — [BCG Forums](https://bcgforums.com/threads/upon-updating-macbook-pro-to-sequoia-15-4-nikon-nef-images-are-no-longer-shown-in-preview-single-view.44000/page-2)
- **ApolloOne:** uses Apple's native decoder plus its own "RawBridge" for bodies Apple does not yet support. Example: 4.1.0 added RawBridge for the Sony A7V, lossless-compressed ARW only, which implies other ARW compression modes were not yet covered on that body. Native Apple decoding was listed for the Nikon Z5 II, Z50 II, Fujifilm X-E5, OM-3, OM-5 II and Sony RX1R III — [App Store listing (snippets)](https://apps.apple.com/gb/app/apolloone-photo-video-viewer/id1044484672). The ZSystemUser page cites ApolloOne and FRV as reading HE files directly — [ZSystemUser](https://www.zsystemuser.com/accessories/versions-of-nikon-software.html). **Camera RawX 2.1.0** added Fujifilm multi-shot RAW — [FujiRumors](https://www.fujirumors.com/?p=140040)
- **AF point per brand:**
  - **Adobe Camera Raw 18.4.1 (2026)** added a "Show Autofocus Points" overlay for Canon, Nikon and Sony raws. Users report it "most of the time" shows nothing for their Sony files, and an August 2026 bug report says it fails on Nikon D850/D500 raws — [BCG thread (snippet)](https://bcgforums.com/threads/adobe-camera-raw-update-18-4-1-show-autofocus-points.56478/latest), [Adobe bug report](https://community.adobe.com/bug-reports-562/p-show-autofocus-points-feature-not-working-in-camera-raw-18-5-for-nikon-d850-or-d500-raw-files-1636010). **New since the spec was written:** Adobe now has AF points, so the spec line "nessuna delle grandi lo fa" needs updating, though Adobe's version is unreliable on Sony.
  - **Lightroom "Focus Points" plugin** (open source): most Nikon and Canon DSLRs, only a few Sony models — [Focus-Points repo mirror](https://git.tdem.in/musselwhizzle/Focus-Points)
  - **Affinity Photo** "Show AF Regions": Canon only, "not 100% reliable" (search snippet) — [DxO forum thread](https://forum.dxo.com/t/add-support-for-display-of-focus-points/27747)
  - **digiKam:** Sony fix after bug 490330 (a6700); 8.8 adds Olympus/OM, with Fujifilm reported working and Pentax in progress — [KDE bug](https://bugs.kde.org/show_bug.cgi?id=490330), [digikam-users](https://mail.kde.org/pipermail/digikam-users/2025-October/037768.html), [Pentax thread](https://mail.kde.org/pipermail/digikam-users/2025-November/037824.html)
  - **Camera RawX:** Canon, Fujifilm, Nikon, OM/Olympus and Sony overlays — [App Store](https://apps.apple.com/us/app/camera-rawx/id6587554858)
  - **ApolloOne:** AF points shown; per-model support is added release by release (e.g. "AF Point support for Nikon Z5 II" in 3.8.0) — [App Store](https://apps.apple.com/gb/app/apolloone-photo-video-viewer/id1044484672)
  - **Sony Imaging Edge:** Sony only (A1, A7S III named) — [Sony](https://support.d-imaging.sony.co.jp/app/imagingedge/en/index.php)
  - **XnView:** a forum request exists for "Display used Autofocus points" — [XnView forum](https://newsgroup.xnview.com/viewtopic.php?p=141987)
  - **FRV:** none, by policy (Q2).
- **Newcomers' brand lists:**
  - **Palomino:** ARW, DNG, 3FR, NEF, CR3, RAF, ORF, HEIC, JPEG and 20+ others — [palomino-app.com](https://palomino-app.com/)
  - **rawcull.com:** ARW, CR2, CR3, NEF, NRW, RAF, ORF, RW2, DNG, PEF, X3F, ERF, MRW, 3FR, MEF and SR2, but needs dcraw via Homebrew for full decoding — [rawcull.com](https://rawcull.com/)
  - **RawCull (netlify docs):** Sony A1 only — [docs](https://rawcull.netlify.app/_print/docs/)
  - **Photo Cull Pro:** a sub-200 ms RAW preview claim with no per-format breakdown — [App Store](https://apps.apple.com/app/id6757907514)
  - **Phiewer Select:** RAW+JPG pairing — [App Store](https://apps.apple.com/app/id6766049040)

### Inferences
- **Speed by format** is mostly determined by the embedded preview, not the RAW codec. The embedded JPEG differs a lot by brand:
  - Sony A1 ARW embeds a full-resolution-class JPEG.
  - Nikon Z NEF embeds full-size.
  - Canon CR3 embeds a full-size JPEG, except HDR/HEIF mode.
  - Fujifilm RAF embeds a smaller preview (often around 1920 px on many bodies).
  - Olympus/OM ORF is often modest.

  This is from general knowledge, **not verified this session**. For brands with small embedded previews, 100% focus checks need a real RAW decode, which is where per-format speed matters (HE NEF and lossy CR3 decode slower).
- **For RawLine's architecture:**
  - Use the embedded preview everywhere, and fall back to Apple ImageIO for the 100% zoom.
  - For Nikon HE on macOS earlier than 26.4, and for bodies Apple does not yet support, plan a fallback: show the embedded JPEG only, and clearly flag "100% from embedded preview" (as FRV did with HE\*). New bodies will lag Apple's RAW updates, which is the same problem ApolloOne solves with RawBridge.
- **AF point is the clearest per-brand gap market-wide:** every implementation is brand- or model-limited and users report silent failures. RawLine should state per-model support openly and show "AF point not available for this body" rather than nothing, which is the behavior Adobe users complain about.
- PM writes metadata *into* ARW/NEF/CR2 when configured. For safety with Lightroom and Capture One, RawLine should stay sidecar-only for all proprietary RAWs and embedded-only for DNG, consistent with PM's own recommendation.

### Gaps
- **No measured per-format benchmarks** (CR3 vs RAF vs NEF HE vs ARW) were found for any app. All speed figures are vendor claims.
- **Format support not checked:**
  - PM: Nikon HE, Canon lossy CRAW, Fujifilm compressed RAF, and new 2025–2026 bodies (e.g. Sony A7V, Nikon Z5 II).
  - Palomino, Photo Cull Pro and others: Nikon HE support.
- The exact Apple RAW support list for macOS 26.x was not fetched (apple.com support page).
- Embedded preview sizes per brand were not sourced; they need a hands-on check with sample files from each brand.
- Adobe's ACR 18.4.1 release date and whether the overlay reaches Lightroom Classic or Bridge were not confirmed (the BCG page returned 403).
