# AI-assisted photo culling apps: state of the market (researched 8 Nov 2026)

Scope note: covers Aftershoot, Narrative (Select), Imagen, FilterPixel, Excire Foto, Optyx, ON1 Photo RAW, Evoto, Lightroom Classic Assisted Culling, Capture One, Luminar Neo, plus newcomers (imagic, PhotoCuller, Retouch4me Arams, small Mac apps). Builds on the spec ("RawLine Selects.md", sections 1, 5.1, 10); I did not repeat its Adobe Community complaint list. Mid-task update from the user: the app must support all camera brands, so each dossier also has a "RAW/brand support" line. **Source caution:** most "best culling software 2026" roundups are written by vendors (Imagen, Aftershoot, FilterPixel, Excire). I trusted vendor docs only for each vendor's own features and pricing, and used independent outlets (PhotoWorkout 5 Nov 2026, Fstoppers 2026, SLR Lounge, PhotoRumors, ShotKit) for judgments. "FilterPass AI" turned up nothing; it is almost certainly FilterPixel. Reddit and FredMiranda returned 403/blocked.

## Per-app dossiers (price, processing, platforms, features, metadata, genres, strengths/weaknesses, changes, RAW support)

### Takeaway
The market has split three ways. **Aftershoot** is turning into a full subscription suite. **Narrative** is the closest to "AI assists, human decides". **Lightroom** now gives away the basic technical checks (eyes, focus, duplicates) inside the catalog. Cheap one-time-purchase local tools (imagic, Excire 2027, ON1 MAX 2027) arrived in late 2026.

### Cited Findings

**Aftershoot (Select / Edit / Retouch / Galleries)**
- Pricing (June 2026): Select about $10/mo billed annually or $15 month-to-month. Edit $30/$35, Retouch $20/$25, Complete (all three) $45/$55. Galleries free with 100 GB, future pricing TBD — [PhotoRumors, 6 Jun 2026](https://photorumors.com/2026/06/06/aftershoot-the-workflow-is-now-complete-and-ai-that-works-for-you-not-against-you/). Confirmed by [PhotoWorkout, 5 Nov 2026](https://www.photoworkout.com/?p=223718): Select $10/mo annual, unlimited images, 30-day trial.
- Black Friday 2026: 25% off annual plans for the first 500 buyers, then 20% — [SLR Lounge](https://www.slrlounge.com/aftershoot-black-friday-2026-25-off-annual-plans-for-the-first-500-buyers-then-20-off/). An October 2026 third-party guide gives conflicting bundle prices ($40/mo Select+Edit), so treat bundle prices as fluid — [search summary, various](https://aftershoot.com/blog/aftershoot-pricing-tiers/).
- Processing: local and offline. Fstoppers quotes the vendor docs: "the AI runs locally, without an internet connection". Cull speed depends on the local GPU, and older machines are slow — [Fstoppers 2026](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026). Windows + macOS — [PhotoWorkout](https://www.photoworkout.com/?p=223718).
- Flat pricing, not per image: a 6,000-frame wedding costs the same as 600 frames — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026).
- Features: burst grouping, duplicate stacks, closed-eye and blur detection, and selection profiles that learn the user's taste — [PhotoWorkout](https://www.photoworkout.com/?p=223718). The May 28, 2026 release added "~20% tighter culls" on duplicates and variations, better blur and closed-eye detection, key-subject prioritization, "cull to target", and **separate labels for "AI Automated" vs "AI Assisted" culls** — [PhotoRumors](https://photorumors.com/2026/06/06/aftershoot-the-workflow-is-now-complete-and-ai-that-works-for-you-not-against-you/).
- Product direction (June 2026): a full RAW editor (masking, denoise, HSL, export JPEG/TIFF) so users "don't need Lightroom". Galleries adds client proofing with print labs. Tethering is a sneak peek, not shipped. Manifesto "AI That Works For You, Not Against You": a pledge not to replace photographers, and to ask permission before training on images — [PhotoRumors](https://photorumors.com/2026/06/06/aftershoot-the-workflow-is-now-complete-and-ai-that-works-for-you-not-against-you/).
- Metadata: ships selects to Lightroom or Capture One — [PhotoWorkout](https://www.photoworkout.com/?p=223718). Ratings read directly into LrC, with a clean handoff to LrC and C1 — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026).
- Genres: weddings and portraits first. Also handled a landscape travel set well — [PhotoWorkout](https://www.photoworkout.com/?p=223718).
- Weaknesses: "confidently wrong" often enough that rejects must be reviewed on important jobs. Cannot recognize the emotionally significant frame. Retouch and Galleries are "new and unproven" — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026).
- RAW/brand support: "all the leading camera manufacturers including but not limited to Canon, Nikon, Fuji, Sony, Olympus, Panasonic" (search snippet; the support page returned 404 on fetch, so I could not read the full list) — [Aftershoot support](https://support.aftershoot.com/en/articles/5353434-what-cameras-does-aftershoot-support).

**Narrative (formerly "Narrative Select")**
- Pricing (help center, "updated this week", Nov 2026), monthly / yearly-per-month: Lite $15/$10, Standard $29/$20, Premium $59/$40, Ultra $79/$60. **The old free plan is retired**, replaced by a 30-day Ultra trial with no card — [Narrative help](http://help.narrative.so/en/articles/7337508-compare-narrative-plans-lite-standard-premium-and-ultra). Fstoppers confirms there is no permanent free plan — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026). (The spec's "Free + Pro ~$15/mo" is outdated.)
- Feature gating: Lite = fast culling, ratings, ship to LR/PS/C1, eye and focus assessment only on hover. Standard and up add Scenes + Image Rank, AI First Pass, Filter by Focus, and the Close-ups panel. "You make the final choice; assessments never delete photos" — [Narrative help](http://help.narrative.so/en/articles/7337508-compare-narrative-plans-lite-standard-premium-and-ultra).
- Processing: culling and assessment run on the user's GPU, files stay on the drive — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026). The help center only says photos "stay where they are"; whether it works fully offline is not stated — [Narrative help](http://help.narrative.so/en/articles/7337508-compare-narrative-plans-lite-standard-premium-and-ultra).
- Strengths: "fastest manual culling interface" in the Fstoppers guide. The Close-Up view speeds focus checks, the user keeps every decision, and selections, ratings and color labels carry into LrC — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026). "Fastest face-by-face check", every face at 100% at once — [PhotoWorkout](https://www.photoworkout.com/?p=223718).
- Weaknesses: slower than fully automated culling on very large shoots. Its editing trails dedicated AI editors. Features are gated by tier — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026).
- Genres: portrait, family, wedding — [PhotoWorkout](https://www.photoworkout.com/?p=223718).
- RAW/brand support: Canon CR2/CR3/CRW, Nikon NEF/NRW, Sony ARW (incl. A7 V, A7R VI), Fujifilm RAF, Panasonic RW2, Olympus ORF, Pentax PEF, Hasselblad FFF/3FR, DNG, RWL, JPEG. HEIC is Mac only. **"New cameras sometimes need a newer version"**. Lightroom Smart Previews cannot be culled — [Narrative help, file types](https://help.narrative.so/en/articles/7337390-what-camera-and-file-types-are-narrative-compatible-with).

**Imagen (AI Culling)**
- Pricing: culling at $12/mo annual ($144/yr) or $18 monthly, unlimited photos. Editing billed separately at $0.05/photo — [PhotoWorkout](https://www.photoworkout.com/?p=223718). Imagen's culling page lists $0.05/photo with $0.01 add-ons for crop, straighten and mask — [Imagen culling (DE)](https://imagen-ai.com/de/culling). One Aug 2026 Imagen blog figure of $0.32/photo conflicts with everything else and is probably an error — [search summary](https://imagen-ai.com/post/how-much-does-photo-editing-cost/). Culling is unlimited inside the "Limitless" plan (~$179/mo yearly per a June 2026 comparison, unverified) — [thewearify](https://thewearify.com/?p=249925).
- Processing: **cloud**. The wedding must be uploaded, which is slow on weak connections and may need a mention in client contracts — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026). PhotoWorkout advises checking data handling if client privacy matters — [PhotoWorkout](https://www.photoworkout.com/?p=223718).
- Personal AI Profile needs at least 2,000 previously edited photos (3,000+ recommended); Talent profiles are the alternative — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026).
- Weakness: a "solid but not as specialized" standalone culler; its value is the editing tie-in — [PhotoWorkout](https://www.photoworkout.com/?p=223718).
- RAW/brand support: not researched (gap).

**FilterPixel** (assumed = "FilterPass AI")
- Pricing: $14.99/mo annual (20 DeepCull shoots/yr), Pro $34.99, Studio $64.99, extra shoots $7.99 each. **Per-shoot quotas** suit spiky seasonal workloads, but heavy shooters outgrow them — [PhotoWorkout](https://www.photoworkout.com/?p=223718).
- Features: basic filters for blur, focus and expression. **DeepCull gives each photo a score plus a written reason** — [PhotoWorkout](https://www.photoworkout.com/?p=223718). Sorts into Accepted / Rejected / Warnings using its own smart previews — [SourceForge summary](https://sourceforge.net/app/filterpixel/web-app/).
- Privacy: originals are not uploaded, but **thumbnails can be sent to its servers for AI training** unless "AI learnings" is turned off — [ShotKit review](https://shotkit.com/filterpixel-review/) (search snippet).
- Vendor admission: generic culling fails at sports because it judges frames in isolation, while sports frames "only make sense in sequence" — [FilterPixel blog](https://filterpixel.com/blog/sports-photo-culling-complete-guide).
- RAW/brand support: not found (gap).

**Excire Foto 2027 / Excire Search**
- $249 one-time ($219 launch price), 14-day trial. Fully local, Windows + macOS. Culling ("Survey Mode", focus peaking, quality scores) is **new in the 2027 release (Oct 2026)**, on top of DAM search by text, face, GPS and OCR — [PhotoWorkout](https://www.photoworkout.com/?p=223718).
- Weakness: the newest culling features in the roundup. Aftershoot is faster and deeper for wedding volume. More of an "AI photo organizer" than a shoot-by-shoot culler — [PhotoWorkout](https://www.photoworkout.com/?p=223718); [search summary](https://excire.com/en/best-culling-software/).
- Excire Search (the Lightroom plugin) was not separately researched (gap).

**Optyx**
- Native Windows + macOS app, processes images locally, but **an internet connection is still needed for the AI analysis**. Its RAW preview speed is a standout, and the free tier is usable just as a fast viewer — [ShotKit](https://shotkit.com/optyx-ai-photo-selection-tool/). v1 Pro was $199.99 on Gumroad and has been superseded by v2 (optyx.app); v2 price not found — [Gumroad](https://optyxapp.gumroad.com/l/MYHep). One roundup gives ~$7/mo and user-defined "Auto-Cull" profiles (unverified, vendor roundup) — [search summary](https://imagen-ai.com/post/best-ai-photo-culling-software-2026/).

**ON1 Photo RAW 2027**
- New **AI Culling Assistant, MAX edition only**: groups visually similar shots, flags closed eyes and out-of-focus frames, batch processing. Announced 8 Sep 2026, shipped 2 Nov 2026. Sold as a one-time purchase or subscription. The page does not say whether processing is local or cloud — [ON1 press release](https://www.on1.com/press/on1-announces-photo-raw-2027-a-new-raw-processing-engine-improved-nonoise-ai-new-ai-culling-assistant-and-more/).

**Lightroom Classic Assisted Culling (Adobe)**
- Mechanism: filters with threshold sliders for Subject Focus, Eye Focus and Eyes Open (plus a "Can't Tell" option). Select/Reject badges. Assisted Culling Info shows the per-photo Subject Sharpness, Eye Sharpness and Eye Open scores. Scores are cached and recomputed after edits — [Adobe help](https://helpx.adobe.com/lightroom-classic/desktop/organize-photos-in-lightroom-classic/assisted-culling.html).
- Changes: Early Access, then GA. 15.2 (Feb 2026) "improved results". Apr 2026: better Subject Focus on shallow depth of field and partially-in-focus subjects. **15.4 (June 2026): per-face panel (Eye Focus / Eyes Open per face) + auto duplicate detection** (Adobe sources conflict on 15.4 vs 15.5 for the Faces panel). 15.6 (Sep 2026) has no culling changes — [Adobe release notes](https://helpx.adobe.com/lightroom-classic/desktop/introduction-to-lightroom-classic/release-notes.html); [LrC 15.4 announcement](https://community.adobe.com/announcements-673/lightroom-classic-v15-4-is-live-cull-people-shots-faster-auto-detect-duplicates-sync-keywords-everywhere-1627070).
- Gaps: no burst grouping, no frame ranking, no learned profile. Weaker than Aftershoot or Imagen for events. Included in Adobe plans — [PhotoWorkout](https://www.photoworkout.com/?p=223718).
- Accuracy: a sports test found it "fairly accurate", and the visible scores let you audit the AI rather than trust it blindly. The same source warns about heat — [Stack Archive](https://stack-archive.com/blog/lightroom-ai-culling-sports-photography-2026). A user saw a shot rejected for subject focus while the eyes scored in focus, and said the scale feels non-linear — [Adobe feedback thread](https://community.adobe.com/questions-675/p-assisted-culling-feedback-thread-lrc-1627467).
- RAW/brand support: whatever Camera Raw supports, since it works inside the catalog (inference). Requires import and previews.

**Capture One**
- No confirmed 2026 AI culling release found. "Face Focus" in Cull and Importer (v16.2) is a face zoom. A C1 staff member said it is not AI culling, because it does not assess sharpness or recommend picks — [C1 community](https://support.captureone.com/hc/de/community/posts/10705908543773-AI-Culling). Aftershoot now works with C1 catalogs — [search summary / Aftershoot blog](https://share.aftershoot.com/?p=54495).

**Evoto / Luminar Neo / Retouch4me**
- Evoto is a retoucher, not a culler. It is cloud-based (servers in Oregon, files deleted after processing) and charges per export credit — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026). I found no evidence of a culling feature.
- Luminar Neo: "has no real culling" — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026).
- Retouch4me "Arams" is a standalone culling and batch app (details not researched) — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026).

**Newcomers (2026)**
- **imagic**: one-time €19 / €49 / €99, fully local, Win + Mac, 500-photo trial. Analyzed 52 HDR frames in 18 s. Sorted 30 keep / 16 review / 6 reject, every reject truly unusable. **Near-duplicates parked for review, not deleted.** Its "Smarter Picks" appeal score is labeled a second opinion only. v1.5 is rough — [PhotoWorkout](https://www.photoworkout.com/?p=223718).
- **PhotoCuller**: PetaPixel (7 Oct 2026) headline says it "keeps you in control of your images". SLR Lounge has a review. Both pages were 403 or unread, so details are a gap — [PetaPixel](https://petapixel.com/2026/10/07/photoculler-speeds-up-your-photo-workflow-and-keeps-you-in-control-of-your-images/); [SLR Lounge](https://www.slrlounge.com/photoculler-review-what-is-photoculler/).
- Other small Mac and App Store apps appeared in search: OptiCull, PickShot, CullAI, Photo Cull Pro, RawCull, Cullit — [App Store OptiCull](https://apps.apple.com/app/apple-store/id6448657895); [PickShot](https://apps.apple.com/app/id6764620388); [RawCull](https://www.itechguides.com/products/rawcull/).

### Inferences
- The industry is converging on the same technical checks: eyes open, eye/subject focus, blur, duplicates. Lightroom ships them for free. Detection alone is no longer a differentiator; **UX speed and trust** are.
- Brand support: only Narrative publishes an explicit list, and it admits new bodies lag behind app updates. That is the same risk for any app that decodes RAW itself. An app that works from the **embedded JPEG preview** (as Photo Mechanic does) supports new cameras on day one for viewing. Separately, Lightroom/Capture One-style apps need their own RAW support. Smart Previews and catalog-only data are not cullable in third-party apps.

### Gaps
- None of the sources said whether each app's AI runs on the embedded preview or on decoded RAW. Aftershoot's camera list page is 404. Imagen, FilterPixel and ON1 brand lists were not checked.
- v2 pricing for Optyx. PhotoCuller details. Retouch4me Arams details.

## Which apps run fully offline on Apple Silicon, and how fast?

### Takeaway
Fully local: Aftershoot, Narrative (GPU), Excire 2027, imagic, and Lightroom (inside the catalog). Optyx is local but needs internet for its AI. Imagen is cloud. FilterPixel keeps originals local but can upload thumbnails. Independent images-per-hour numbers almost do not exist.

### Cited Findings
- Aftershoot works offline. Speed depends on the GPU, and old machines are slow — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026).
- Narrative's assessments run on the user's GPU — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026).
- imagic: 52 frames in 18 s (~10,000/hour extrapolated, on unknown hardware) — [PhotoWorkout](https://www.photoworkout.com/?p=223718).
- Optyx needs internet for its AI even though processing is local — [ShotKit](https://shotkit.com/optyx-ai-photo-selection-tool/).
- Imagen is cloud only — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026).
- Lightroom has a background analysis indicator, and analysis is a separate step after import — [Adobe release notes](https://helpx.adobe.com/lightroom-classic/desktop/introduction-to-lightroom-classic/release-notes.html).

### Inferences
- An app with no pre-analysis wait (the user starts culling right away while AI fills in later) would beat every competitor on time-to-first-photo. All of them analyze first.

### Gaps
- No independent images-per-hour benchmarks on M-series Macs for Aftershoot, Narrative or Lightroom. Vendor claims (e.g. Aftershoot's "60+ days/year saved") are unverified.

## How do pros rate the accuracy of AI picks?

### Takeaway
The consensus is consistent: reliable for technical rejects (blinks, missed focus, duplicates), unreliable for emotional or decisive keepers. Rejects must be reviewed. Sports and wildlife are weak spots because frames are judged one at a time and the models are trained on people.

### Cited Findings
- "Reliable for technical rejects... not for emotional keepers", review rejects on paid jobs. Aftershoot is "confidently wrong" — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026).
- Sports: frames "only make sense in sequence" (vendor admission) — [FilterPixel](https://filterpixel.com/blog/sports-photo-culling-complete-guide). A rugby photographer on FredMiranda doubts AI culling can work, since even photographers lack a consistent logic for picks (search snippet; page 403) — [FredMiranda](https://www.fredmiranda.com/forum/topic/1894748).
- Lightroom's subject and eye scores contradict each other in a user report — [Adobe thread](https://community.adobe.com/questions-675/p-assisted-culling-feedback-thread-lrc-1627467).
- imagic's rejects were all genuinely unusable in a small test — [PhotoWorkout](https://www.photoworkout.com/?p=223718).
- (Also see spec section 10: G2 complaints that the AI picks the wrong photos and misses emotional moments, and that it does not see eyes on distant birds.)

### Gaps
- No systematic independent accuracy study found. Wildlife-specific culling accuracy reports were not found (searches returned AI-generated-imagery stories instead).

## Which features are loved vs ignored?

### Takeaway
Loved: face close-ups or per-face panels, duplicate/burst stacks, blink and focus flags, explanations of scores, and LR/C1 handoff. Treated with suspicion: auto-select, "AI picks", and personal profiles that need thousands of edits.

### Cited Findings
- Narrative Close-ups is the "fastest face-by-face check". The user keeps every decision — [PhotoWorkout](https://www.photoworkout.com/?p=223718); [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026).
- Adobe added a per-face panel and duplicates in 15.4 as the headline "cull people shots faster" — [Adobe announcement](https://community.adobe.com/announcements-673/lightroom-classic-v15-4-is-live-cull-people-shots-faster-auto-detect-duplicates-sync-keywords-everywhere-1627070).
- Explainability as a selling point: FilterPixel DeepCull writes a reason per photo — [PhotoWorkout](https://www.photoworkout.com/?p=223718). Lightroom's visible scores let you "audit" the AI — [Stack Archive](https://stack-archive.com/blog/lightroom-ai-culling-sports-photography-2026).
- Even Aftershoot now labels "AI Automated" vs "AI Assisted" culls and published an "AI that works for you" manifesto. Vendors are responding to trust concerns — [PhotoRumors](https://photorumors.com/2026/06/06/aftershoot-the-workflow-is-now-complete-and-ai-that-works-for-you-not-against-you/).
- The Imagen profile needs 2,000–3,000 edited photos — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026).

### Gaps
- No usage data on which features people actually ignore. This is inferred from reviews.

## Pricing backlash and business models

### Takeaway
Subscriptions dominate (Aftershoot, Narrative, Imagen, FilterPixel). Narrative removed its free plan. In late 2026, one-time purchases came back as a counter-trend (imagic €19–99, Excire $249, ON1 MAX). Per-image and per-shoot pricing persists at Imagen and FilterPixel.

### Cited Findings
- Narrative's free plan is retired. Prices run $10–$60/mo yearly — [Narrative help](http://help.narrative.so/en/articles/7337508-compare-narrative-plans-lite-standard-premium-and-ultra).
- Aftershoot Complete is "one of the pricier subscriptions" — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026). Discounts are heavy (BF 25%) — [SLR Lounge](https://www.slrlounge.com/aftershoot-black-friday-2026-25-off-annual-plans-for-the-first-500-buyers-then-20-off/).
- One-time options: imagic, Excire — [PhotoWorkout](https://www.photoworkout.com/?p=223718). ON1 — [ON1](https://www.on1.com/press/on1-announces-photo-raw-2027-a-new-raw-processing-engine-improved-nonoise-ai-new-ai-culling-assistant-and-more/).
- Imagen's "$10 AI editing offer" started a "peak-season price war" (headline only) — [PhotoWorkout](https://www.photoworkout.com/?p=221310).

### Inferences
- Bundling (culling + edit + gallery) is how vendors justify subscriptions. A standalone culler is commoditizing toward cheap or free, which supports RawLine's free beta.

### Gaps
- No direct forum-sourced backlash quotes from 2026 (Reddit and FredMiranda blocked). See spec item 18 for earlier evidence.

## Which AI features save time without taking the decision away?

### Takeaway
The features pros praise most are "where to look" aids, which matches RawLine's principle: per-face close-ups, burst and duplicate grouping, focus visualization, and explanations. Auto-select and ranking are where trust breaks.

### Cited Findings
- Narrative is praised because the photographer still makes every selection while the AI flags eyes, near-duplicates and auto-zooms to faces — [Fstoppers](https://fstoppers.com/best-ai-retouching-and-culling-tools-2026).
- imagic parks near-duplicates for review instead of deleting them, and labels its appeal score a "second opinion" — [PhotoWorkout](https://www.photoworkout.com/?p=223718).
- Excire uses focus peaking as a culling aid — [PhotoWorkout](https://www.photoworkout.com/?p=223718).
- Capture One's own staff distinguish face zoom from "AI culling" — [C1 community](https://support.captureone.com/hc/de/community/posts/10705908543773-AI-Culling).

### Inferences
- RawLine's planned set (face strip, burst grouping, AF-point zoom, peaking) lines up with the most-praised features, and avoids the most-criticized one (auto picks). The differentiators still open: no wait before culling, AF-point overlay across brands, and video.
- Note for the spec: Narrative's free plan is gone, and Lightroom now has per-face scores and duplicates, so section 1's tables need updating.

### Gaps
- No controlled time-saved study separating "assist" features from "auto-select".
