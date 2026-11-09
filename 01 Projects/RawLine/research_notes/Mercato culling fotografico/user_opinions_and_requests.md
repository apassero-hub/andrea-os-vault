# Photographer opinions on culling tools: pain points and unmet requests (2023–2026)

Research date: 8 Nov 2026. Scope: going beyond section 10 of "RawLine Selects.md" (24 pains already listed there are not repeated unless new evidence was found). All brands covered (Sony, Canon, Nikon, Fujifilm, Panasonic, OM System, Leica, Hasselblad), per the coordinator's update.

Method note: Reddit, Fred Miranda, BCG Forums and MacRumors all returned HTTP 403 to the fetch tool, and web search did not surface Reddit threads. The primary sources actually read were the Adobe Community (feature requests plus the Assisted Culling feedback thread), TalkPhotography, FastRawViewer, the Capture One community, Apple Discussions and the Canon community. Several search-result summaries were vendor blogs (Aftershoot, FilterPixel, Imagen, Kepla), so they are flagged as biased. Frequency labels (High / Medium / Low) are my own estimates from how many independent threads and sources raised each issue in this pass. They are not measured counts.

## 1. Speed and lag (previews, 100% zoom, big files, external/network drives)

### Takeaway
Lag is still the number one pain, and it is getting worse as files grow (Sony A1, Nikon Z9, drones). It shows up most in Lightroom, and lately also in Photo Mechanic on new macOS versions (already in spec #4). Users keep recommending one fix: "cull from embedded JPEG before import."

### Cited Findings
- (High) A Lightroom Classic user (Dec 2025) culling Sony A1 and DJI Mavic 4 Pro RAWs from a CFexpress card via USB reader says culling "all of a sudden became incredibly slow" after an update, with every frame taking a moment to load, which makes a 2,000-frame card frustrating. Sony A9II files from the same setup were still fast. Purging the cache, switching the GPU to display-only and using an older catalog did not help. A community expert advised importing to the internal drive first, or using Photo Mechanic. — [Adobe Community, 21 Dec 2025](https://community.adobe.com/questions-675/lightroom-culling-larger-raw-files-slowed-with-new-update-1617607)
- (Medium) A Nikon Z9 user calls Lightroom Classic 11.2 import thumbnails "almost unusable". Only the thread title was seen; the content was not read. — [Adobe Community](https://community.adobe.com/questions-675/lr-classic-11-2-very-slow-presenting-nikon-z9-import-thumbnails-almost-unusable-960571)
- (Medium) A tester running about 5,000- and 1,100-image sets says Lightroom needs full-size previews to cull and gets slower over time, and that culling before import is the real value. — [TalkPhotography FaceCull thread, Oct 2026](https://www.talkphotography.co.uk/threads/facecull-anyone-want-to-test-a-fast-culling-app-for-events.776973/)
- (Medium) The FastRawViewer speed advantage disappears on Adobe-converted DNGs. One user found that once Lightroom converts a shoot to DNG, "all speed is lost". This matters for anyone who converts to DNG, and for Leica/Pentax native DNG users. — [FastRawViewer forum](https://www.fastrawviewer.com/node/540)
- A Leica Q user says Photo Mechanic is fast only because it shows the embedded JPEG inside the DNG. Switching to rendering the DNG itself would lose the speed. — [L-Camera Forum tag page](https://www.l-camera-forum.com/tags/Photo%20Mechanic/)
- Photo Mechanic's documentation confirms it displays the RAW's embedded JPEG "for the fastest browsing experience". — [Camera Bits docs](https://docs.camerabits.com/support/solutions/articles/48000361354-supported-file-formats)
- One competitor review flags Narrative Select as slower than FilterPixel and Aftershoot (vendor-biased source). Another review flags Excire 2025's slow import. — [Digital Camera World roundup](https://digitalcameraworld.com/buying-guides/best-photo-culling-software); [Excire 2025 review](https://ahutchinson.substack.com/p/excire-2025-indepth-review-a-lightning)

### Inferences
- File size is the trigger. The same pipeline is fine for 24 MP and breaks for 50 MP or larger. RawLine's "embedded preview first, full RAW decode only on demand" is the right call, but it has to cope with bodies whose embedded JPEG is small (see section 9).
- Culling straight from card readers, CFexpress and USB drives is normal practice, so I/O-bound prefetch matters as much as decode speed.

### Gaps
- No Reddit or DPReview speed threads could be read (403 / no results).
- No measured comparison across apps of time-to-100%-zoom on 50 MP files was found.

## 2. Burst / sequence culling (sports, wildlife, birds in flight)

### Takeaway
"Pick the sharpest of N near-identical frames" is the oldest open request in this space (Adobe idea open since 2011, marked released only in Feb 2026 via Assisted Culling). Wildlife shooters say the general-purpose AI tools don't serve them. A wave of small indie burst-culling apps (2025–2026) shows that demand is still unmet.

### Cited Findings
- (High) An Adobe idea, "find the sharpest photo based on the eyes", opened in Jun 2011, collected 17 votes, 14 replies and about 2.9k views. It was marked "Released" on 5 Feb 2026, pointing to Assisted Culling. Comments along the way:
  - a 2021 request for a button that ranks a burst by face sharpness
  - a 2023 request for a sharpness overlay scaled to high-MP files and pre-generated per folder
  - a 2025 complaint that it had taken almost 15 years
  - suggestions to select a region of interest and rank frames by high-frequency detail
  — [Adobe Community](https://community.adobe.com/feature-requests-676/p-find-the-sharpest-photo-based-on-the-eyes-666325)
- (High) A Sept 2026 Lightroom request asks for three things: (1) show the AF point, (2) AI comparison of edge detail inside a user-chosen area across 2+ images, with a different area allowed per image to follow a moving subject, (3) an adjustable edge-detection view shown side by side. The poster says culling thousands of wildlife images is very time consuming. Adobe moved parts 2 and 3 to Ideas as new requests; the AF-point part duplicates an existing request. — [Adobe Community, 21 Sep 2026](https://community.adobe.com/feature-requests-676/p-side-by-side-sharpness-comparison-for-photo-culling-1643207)
- (High) A 20 fps birds-in-flight shooter says culling reached "a whole new level of tediousness". They now drop to 10 fps when that is enough, and bought FastRawViewer. Same user: 1 TB won't hold 18,000 A1 RAWs, and 2 TB is barely enough. — [BCG Forums "Culling in the field"](https://bcgforums.com/threads/culling-in-the-field.16795/page-3) (content via search summary; page 403)
- Sony A1 buffer: about 127–128 frames at 30 fps before slowing (Fred Miranda tester). 30 fps only with lossy compressed RAW; lossless compressed tops out at 20 fps. This defines the typical burst size to cull. — [Fred Miranda](https://www.fredmiranda.com/forum/topic/1685804/21/); [DPReview A1 review](https://www.dpreview.com/reviews/sony-a1-review)
- (Medium, a market signal) Several indie burst cullers launched or recruited testers in 2025–2026, each positioned on "the subject sharp, not the branch":
  - BurstPick: groups bursts, scores subject edge sharpness, offline
  - Wildlife Engine: eye sharpness and species
  - Tack: local, birds
  - Picturesque: open source
  - a BCG "alpha testers wanted" local burst-culling app

  Requests raised in those threads include handling birds facing away, heads turned, or subjects clipped by the frame edge. — [BurstPick](https://burstpick.com/); [BCG BurstPick 1.0](https://bcgforums.com/threads/burstpick-1-0-release.55925/); [Wildlife Engine](https://wildlifeengine.com/); [Picturesque](https://denyszorinets.github.io/picturesque/); [BCG alpha testers](https://bcgforums.com/threads/looking-for-4-alpha-testers-%E2%80%94-local-burst-culling-app-for-wildlife-photography.54652/)
- In the past Aftershoot staff said they had no AI built for wildlife (older comment, via search summary). — [BCG "AI for culling and editing"](https://bcgforums.com/threads/ai-for-culling-and-editing.35196/)
- A motorsport tester (cars and bikes) finds auto sharpness rating "only about 90% accurate" but praises sequence comparison for picking the sharpest frame. — [TalkPhotography, Oct 2026](https://www.talkphotography.co.uk/threads/facecull-anyone-want-to-test-a-fast-culling-app-for-events.776973/)

### Inferences
- A burst view that auto-groups by timestamp, ranks frames by sharpness at the AF point or subject, and keeps zoom and position locked while you step through is the clearest unmet need. Today it is spread across niche wildlife apps that lack Photo Mechanic-class speed and metadata reliability.
- About 90% accuracy is "good but you still check every frame". The UI should make verifying fast rather than hide frames.
- A per-image region of interest (the subject moves between frames) is a specific, rarely offered detail.

### Gaps
- No user-reported accuracy comparisons across BurstPick, Wildlife Engine and Tack were found.

## 3. Focus checking (AF point, eye, sharpness comparison, synced zoom)

### Takeaway
Users want an AF-point overlay and a "zoom to AF point" action on every brand. Many tools refuse because the makernotes are undocumented. The demand is persistent (2015 to 2026), and an overlay with honest caveats would set an app apart.

### Cited Findings
- (High) FastRawViewer request (Dec 2021): show the focus point when culling fast-moving bursts. The user currently pre-culls in Sony Imaging Edge to see AF points. The developer (LibRaw) declined on the same day. Their reasons: focus tags are undocumented and must be verified per body and firmware, ExifTool's data has errors, focus-and-recompose makes the data misleading, and they "cannot guarantee" it works. — [FastRawViewer node/826](https://www.fastrawviewer.com/node/826)
- (Medium) The same request dates back to 2015 in IMatch, where the answer was that it is vendor-specific and depends on the camera writing the tags. — [photools forum](https://photools.com/community/index.php?msg=27370)
- (Medium) The AF-point display request already exists at Adobe (staff say it is "already tracked"), and a commenter says it "probably isn't hard to build". — [Adobe Community, Oct 2026](https://community.adobe.com/feature-requests-676/p-side-by-side-sharpness-comparison-for-photo-culling-1643207)
- (Medium) FaceCull, an indie Mac event culler, zooms to the AF point when no face is found. In Oct 2026 the developer was asking for Sony, OM System and non-Z8 Nikon testers to extend AF-point support. This confirms that per-brand AF parsing is the bottleneck. — [TalkPhotography](https://www.talkphotography.co.uk/threads/facecull-anyone-want-to-test-a-fast-culling-app-for-events.776973/)
- (Medium) Focus-mask / focus-peaking overlay requests (2023, 2025) and a long-running "focus mask image sharpness" idea for Camera Raw. — [Adobe idea 666325](https://community.adobe.com/feature-requests-676/p-find-the-sharpest-photo-based-on-the-eyes-666325); [Adobe "focus mask" idea](https://community.adobe.com/feature-requests-564/p-focus-mask-image-sharpness-666529/index1.html)
- One accessibility angle: the Sept 2026 requester has vitreous floaters that make visual comparison of fine detail hard, and wants a machine-measured sharpness view. — [Adobe Community](https://community.adobe.com/feature-requests-676/p-side-by-side-sharpness-comparison-for-photo-culling-1643207)

### Inferences
- Ship the AF-point overlay per brand in tiers ("verified" vs "experimental"), and label it honestly (for example "AF point at capture; may differ after recompose"). That answers LibRaw's objection without withholding the feature.
- A focus-peaking overlay on the full-res preview, plus a numeric sharpness score inside the AF box, would cover both the human check and the accessibility case.

### Gaps
- No brand-by-brand list was found of which makernotes reliably store the AF point (Canon CR3, Nikon NEF/HE, Fuji RAF, OM ORF, Panasonic RW2, Hasselblad 3FR). This needs an ExifTool test-file survey.

## 4. Metadata / interoperability (Lightroom, Capture One, in-camera ratings)

### Takeaway
Interop failures cluster in three places:
- color labels, which are not standardized
- Capture One reading labels back
- in-camera ratings disappearing on import

The last one hits every brand and was not in spec section 10.

### Cited Findings
- (High) Capture One + Photo Mechanic users report:
  - Capture One writes `xmp:Label` but does not read it back
  - ratings come through fine but color labels don't (stars are standardized, labels aren't)
  - the fifth label must be named Pink or Purple to map
  - case-sensitive storage breaks `.XMP` vs `.xmp` lookups
  - drag-and-drop from Photo Mechanic to Capture One loses stars and labels
  
  — [Capture One "Metadata sync"](https://support.captureone.com/hc/de/community/posts/360009386958-Metadata-sync); [Capture One "Importing Ratings and Colour Tags"](https://support.captureone.com/hc/en-us/community/posts/360012347678-Importing-Ratings-and-Colour-Tags); [Capture One drag-and-drop thread](https://support.captureone.com/hc/fr/community/posts/4405130944541-Drop-and-Drag-Directly-from-Photo-Mechanic-to-Capture-one-not-recognizing-star-ratings-or-color-labels); [jmpeltier.com PM + C1 workflow](https://www.jmpeltier.com/photo-mechanic-capture-one-workflow/)
- (High, all brands) In-camera star ratings lost or not shown in Lightroom:
  - Canon 5D IV, R7 (Nov 2023), R6
  - Nikon D850, and ratings set in Nikon ViewNX-i
  - German-language threads
  
  Diagnosed causes:
  - with two cards, the camera writes the rating only to the primary card
  - an import metadata preset overwrites ratings to 0
  - the rating is applied only to the RAW or only to the JPEG of a pair
  - Canon R video ratings live in `QuickTime:Rating` and don't survive import
  
  — [Adobe: 5D IV](https://community.adobe.com/questions-675/5d-mk4-star-rating-not-showing-in-lightroom-985735); [Canon community: R7, Nov 2023](https://community.usa.canon.com/t5/EOS-DSLR-Mirrorless-Cameras/Photo-Ratings-Assigned-on-R7-Not-Showing-Up-on-Computer/m-p/445594); [Canon community: R6](https://community.usa.canon.com/t5/EOS-DSLR-Mirrorless-Cameras/EOS-R6-star-ratings-don-t-transfer-into-Lightroom/m-p/577490); [Adobe: Canon R video ratings](https://community.adobe.com/questions-675/rating-videos-on-camera-canon-r-stars-don-t-survive-import-to-lr-classic-976090); [Adobe: D850](https://community.adobe.com/questions-680/import-with-image-rating-from-nikon-d850-928805); [Adobe: ViewNX-i](https://community.adobe.com/questions-675/nikon-viewnx-i-ratings-not-showing-up-in-lr-cc-984578); [Adobe: "ratings made on camera no longer imported"](https://community.adobe.com/questions-675/star-ratings-made-on-camera-are-no-longer-being-imported-to-desktop-977498)
- (Medium) A bug report says many CR3 metadata fields are not imported by Lightroom (title only seen). — [Adobe bug report](https://community.adobe.com/bug-reports-562/p-many-metadata-fields-in-cr3-files-not-imported-666832/index3.html)
- (Medium) Assisted Culling (LrC 15.5.1, Sept 2026): after a 2,000-image Canon cull, images "lose their Reject status" when you pause on them, and a frame's focus score jumped from under 30 to 64 between runs. — [Adobe Assisted Culling feedback thread](https://community.adobe.com/questions-675/p-assisted-culling-feedback-thread-lrc-1627467/index3.html)

### Inferences
- New, all-brand feature: on ingest, read in-camera ratings and protect flags from both cards and both members of a RAW+JPEG pair (including Canon `QuickTime:Rating` on video), merge them, and show "N in-camera ratings found". No tool advertises this.
- Offer one-click label presets ("Capture One", "Lightroom EN/IT", "Photo Mechanic"), and write lowercase `.xmp` sidecars by default or make the case configurable.

### Gaps
- Behavior of Fuji, OM System, Panasonic and Hasselblad in-camera ratings on import was not found.

## 5. Pricing, subscriptions and trust in AI picks

### Takeaway
Subscription fatigue is strong and widely voiced. The Photo Mechanic subscription switch (Nov 2023) pushed some users away. Trust in AI picks is low for events and wildlife: users want suggestions they can review, not automatic decisions, and they want repeatable scores.

### Cited Findings
- (High) Camera Bits moved Photo Mechanic to subscription-only in Nov 2023, and perpetual licenses stopped getting major updates. — [PetaPixel, 15 Nov 2023](https://petapixel.com/2023/11/15/photo-mechanic-caves-to-industry-trends-shifts-to-subscription-model); [Camera Bits](https://home.camerabits.com/changes-coming-to-photo-mechanic/)
- Prices differ across sources: Plus at $249/yr ([baty.net, Jun 2024](https://baty.net/2024/06/photo-mechanic-2024)); standard at $14.99/mo, $149/yr or $299 once per a 2026 list ([Kepla](https://www.getkepla.com/blog/photo-mechanic-alternatives)). These conflict with other quotes; verify on camerabits.com.
- (Medium) Reactions:
  - a blogger who couldn't find a replacement and subscribed anyway ("expensive, but better")
  - Fred Miranda users who switched to alternatives after the change
  - an Fstoppers piece pleading to "save us from all these subscriptions"
  - an Oct 2026 TalkPhotography developer who says Photo Mechanic was "reaching end of life" on his Mac
  
  — [baty.net](https://baty.net/2024/06/photo-mechanic-2024); [Fred Miranda](https://www.fredmiranda.com/forum/topic/1944002/) (403, via search summary); [Fstoppers](https://fstoppers.com/business/someone-please-save-us-photographers-all-these-subscriptions-649634); [TalkPhotography](https://www.talkphotography.co.uk/threads/facecull-anyone-want-to-test-a-fast-culling-app-for-events.776973/)
- Price pressure around the market: Adobe's photography plan rose (2025), and Capture One raised all prices 6% (May 2026). — [Digital Camera World](https://www.digitalcameraworld.com/tech/software/adobe-lightroom-and-photoshop-cost-increasing-for-2025); [PetaPixel, 27 May 2026](https://petapixel.com/2026/05/27/capture-one-to-increase-all-product-prices-by-6/)
- Aftershoot's 2026 tiers have no per-photo charges, with prices locked through Apr 2028. A founders "Complete" plan costs $499/yr, and one user reported paying $40/mo for Pro. I found no evidence of a 2025 backlash. — [Aftershoot pricing](https://aftershoot.com/blog/aftershoot-pricing-tiers/); [PricingSaaS](https://pricingsaas.com/companies/aftershoot)
- (High) Trust in AI from the Lightroom Assisted Culling feedback thread (Aug–Sep 2026):
  - all 1,877 event photos rejected at default-high thresholds
  - background people counted as subjects
  - "similar" stacks group scenes wrongly
  - results change on every re-check
  - eye detection right about 70% of the time
  - it "took longer than manual culling"
  - requests for it to propose a set without changing the user's own selections, a permanent off switch, a confirmation before batch runs, and progress shown in the standard progress bar
  
  — [Adobe feedback thread](https://community.adobe.com/questions-675/p-assisted-culling-feedback-thread-lrc-1627467/index3.html)
- Press: TechRadar calls it the most useful AI in LrC 2026, with variable results. Digital Camera World calls it a great idea but "really annoying". — [TechRadar](https://www.techradar.com/pro/software-services/adobe-lightroom-classic-2026-review?type=Review); [DCW](https://www.digitalcameraworld.com/tech/software/lightroom-classics-assisted-photo-culling-is-a-great-idea-but-is-really-annoying-but-i-have-found-a-solution)
- One competitor claims Aftershoot downgrades atmospheric concert and stage-light frames (vendor-biased). A Dec 2025 G2 reviewer says AI services didn't fit their workflow and Photo Mechanic is "the absolute fastest". — [FilterPixel blog](https://filterpixel.com/blog/aftershoot-alternative); [G2 Camera Bits](https://www.g2.com/sellers/camerabits)

### Inferences
- Deterministic, explainable scores (same input, same score) are a selling point in their own right, since score drift is a top complaint.
- "AI proposes in a separate layer, never touches my flags" is explicitly requested, which validates spec 5.1.

### Gaps
- No Reddit sentiment counts were found. Narrative's current pricing complaints were not found.

## 6. Video clips, RAW+JPEG pairs, dual card, ingest

### Takeaway
Hybrid shooters split stills and clips at ingest because no culler handles both well. RAW+JPEG and dual-card setups quietly break ratings. Brand-new bodies often can't be decoded at all.

### Cited Findings
- (Medium) No mainstream culler handles mixed photo and video culling. Imagen's keyframe extraction is the only video-adjacent feature found (vendor claim). Narrative Select is photo-only. — [Imagen hybrid guide](https://imagen-ai.com/valuable-tips/ai-photo-editing-for-hybrid-shooters-guide-2026/); [Narrative](https://narrative.so/blog/narrative-review)
- (Medium) Canon R in-camera video ratings are lost on import. — [Adobe Community](https://community.adobe.com/questions-675/rating-videos-on-camera-canon-r-stars-don-t-survive-import-to-lr-classic-976090)
- (Medium) With dual cards, the rating is written only to the primary card, and the rating lands on only the RAW or only the JPEG. — [Adobe: 5D IV](https://community.adobe.com/questions-675/5d-mk4-star-rating-not-showing-in-lightroom-985735)
- Desired: one-step copy + rename + backup + cull (spec #20; see also a FastRawViewer "culling during import?" thread). — [FastRawViewer node/909](https://www.fastrawviewer.com/node/909)
- Ingest-speed wish from a motorsport tester: bulk reject and delete in as few steps as possible, and move rejects to the Trash with undo. — [TalkPhotography](https://www.talkphotography.co.uk/threads/facecull-anyone-want-to-test-a-fast-culling-app-for-events.776973/)

### Inferences
- Treat a RAW+JPEG pair and a dual-card mirror as one logical image, so a rating applied to one applies to all copies.

### Gaps
- No user threads specifically about Sony XAVC / Canon / Nikon N-RAW clip culling in Photo Mechanic were found.

## 7. Client proofing, collaboration, iPad / travel culling

### Takeaway
Photo Mechanic has no iPad version. iPad culling relies on minor apps or the Lightroom cloud sync workaround. Requests for field culling exist, but this pass found less volume here than for speed and focus.

### Cited Findings
- (Medium) Photo Mechanic has no iPad version. A wedding pro's workaround is to pre-cull in Photo Mechanic on the desktop, then use Lightroom sync to the iPad. — [Shotkit iPad Pro workflow](https://shotkit.com/mobile-workflow-solution-ipad-pro/)
- iPad apps in use: PhotoPicker (culls from card or Files and writes XMP; reviews mixed) and Photo Workflow ($4.99). — [PhotoPicker on the App Store](https://apps.apple.com/us/app/-/id650580494); [Photo Workflow](https://apps.apple.com/us/app/photo-workflow/id6447488209)
- (Low–Medium) A BCG thread on iPad culling while traveling. — [BCG](https://bcgforums.com/threads/workflow-for-downloading-and-culling-pictures-on-an-ipad-while-traveling.35338/) (403)
- Narrative markets a combined cull, edit, review and deliver flow, which suggests vendors see proofing as the next step. — [Narrative blog](https://narrative.so/blog/smarter-workflow-for-modern-photographers)

### Gaps
- No primary user complaints were found about proofing or collaboration inside culling apps. Most of this sits on Pixieset/Pic-Time, outside scope.

## 8. UI / ergonomics: keyboard, controllers, fatigue

### Takeaway
Controller use is common, but mapping is clumsy. Users want relative rating (+/- star) on dials, direct 1–5 buttons, and gamepad support without third-party mappers. Loupedeck hardware is discontinued, which strands some users.

### Cited Findings
- (Medium) A TourBox Neo user can't map the dial to set star ratings and wants direct 1–5 buttons. They note Camera Bits was working on relative "rating up/down" shortcuts. — [ishootshows TourBox Neo review](https://ishootshows.com/tourbox-neo-review-for-photographers/)
- (Medium) Gamepads on Mac need $5–8 key-mapping apps, about $180 all-in with Photo Mechanic. — [Fstoppers](https://fstoppers.com/originals/how-speed-your-culling-process-128294)
- Fstoppers' 2026 guide notes that the Stream Deck makes you look down while the TourBox lets your eyes stay on the image. Logitech stopped selling Loupedeck hardware in 2025, and one reviewer calls Loupedeck "horrible for culling". — [Fstoppers 2026](https://fstoppers.com/guide/best-editing-consoles-and-control-surfaces-2026); [Photography Life Loupedeck](https://photographylife.com/reviews/loupedeck-lightroom-editing-console)
- Accessibility and fatigue: vitreous floaters make fine-detail comparison hard, so the user wants a machine sharpness view. Consoles are pitched as reducing repetitive strain. — [Adobe, Sep 2026](https://community.adobe.com/feature-requests-676/p-side-by-side-sharpness-comparison-for-photo-culling-1643207); [Imagen shortcuts post](https://imagen-ai.com/post/lightroom-culling-shortcuts/)
- Lightroom batch-selecting to apply ratings is awkward (Aug 2026). — [Adobe feedback thread](https://community.adobe.com/questions-675/p-assisted-culling-feedback-thread-lrc-1627467/index3.html)

### Inferences
- Native support should cover the Game Controller framework (no mapper needed), MIDI, and relative rating commands for dials (TourBox, MX Creative Console).

### Gaps
- No user data on Stream Deck plugins for culling apps was found.

## 9. Brand-specific issues (all brands)

### Takeaway
Problems outside Sony mostly come from (a) brand-new bodies or compression modes the RAW decoders don't support yet (Nikon HE/HE*, new Canon CR3 bodies, compressed RAF on macOS), (b) embedded previews that are small or use odd JPEG encodings (Fuji), and (c) in-camera ratings lost on import (Canon, Nikon).

### Cited Findings
- (High) **Nikon Z8/Z9 HE/HE\* NEF**: LibRaw-based apps treat these files as corrupted. The Tonfotos vendor confirms it has no support because LibRaw lacks it. — [Tonfotos community](https://community.tonfotos.com/d/1094-support-for-nef-files-when-high-efficiency-option-is-activated)
- (Medium) **Nikon Z9**: Lightroom import thumbnails "almost unusable" (LrC 11.2). — [Adobe](https://community.adobe.com/questions-675/lr-classic-11-2-very-slow-presenting-nikon-z9-import-thumbnails-almost-unusable-960571)
- (High) **Canon CR3 / new bodies**:
  - LibRaw did not support the R3 (Topaz thread)
  - there are R6 Mark III RAW loading issues
  - macOS Preview couldn't open R6 II CR3 until Apple updated it
  - CR3 metadata fields go missing in Lightroom
  - ratings are lost (R7, R6, 5D IV)
  
  — [Topaz](https://community.topazlabs.com/t/canon-cr3-raw-support/13891?page=2); [Canon: R6 III](https://community.usa.canon.com/t5/EOS-DSLR-Mirrorless-Cameras/EOS-R6-Mark-III-Issues-with-loading-RAW-files/m-p/577316); [Canon: R6 II macOS Preview](https://community.usa.canon.com/t5/Camera-Software/Preview-not-opening-R6-mark-ii-CR3-RAW-files-in-macOS/m-p/399626); [Canon: R7 ratings](https://community.usa.canon.com/t5/EOS-DSLR-Mirrorless-Cameras/Photo-Ratings-Assigned-on-R7-Not-Showing-Up-on-Computer/m-p/445594)
- (Medium) **Fujifilm compressed RAF**: macOS, iOS and iPadOS could not open compressed RAF (May 2024), though uncompressed RAF works. The user wanted at least the embedded JPEG shown in Finder. A reply explains that Apple adds support per model and per OS release only. — [Apple Discussions](https://discussions.apple.com/thread/255613945)
- (Medium) **Fujifilm embedded previews** use unusual JPEG variants (SOF1 extended sequential, odd APP0 lengths, multiple preview streams), which trip up naive extractors. — [Starsky docs](https://qdraw.github.io/starsky/docs/advanced-options/thumbnail-generation/raw-embedded-preview-extraction)
- (Medium) **Embedded preview size varies by body**: some bodies embed a full-res JPEG, others only about 2048 px. Some cameras let you set the preview size separately. A small preview makes culling at 100% impossible without a full RAW decode. — [havecamerawilltravel](https://havecamerawilltravel.com/workflow/extract-jpg-raw-2/)
- **Leica (DNG)**: fast in Photo Mechanic only through the embedded preview. Adobe-converted DNGs lose FastRawViewer's speed. — [L-Camera Forum](https://www.l-camera-forum.com/tags/Photo%20Mechanic/); [FastRawViewer](https://www.fastrawviewer.com/node/540)
- **OM System**: FaceCull's developer is seeking OM System testers to add AF-point support, a sign that ORF AF data is still unparsed in indie tools. — [TalkPhotography](https://www.talkphotography.co.uk/threads/facecull-anyone-want-to-test-a-fast-culling-app-for-events.776973/)
- Vendor workarounds for unsupported bodies are clumsy: Narrative tells users to shoot RAW+JPEG and cull the JPEGs, or convert to DNG first. — [Narrative help](https://help.narrative.so/en/articles/7337390-what-camera-and-file-types-are-narrative-compatible-with)

### Inferences
- RawLine on macOS depends on Apple's RAW engine (or LibRaw) for full decode, so new-body lag is a real risk. A fallback that always shows the embedded JPEG, even for unsupported RAWs, plus a clear "embedded preview only, X px" badge, would turn a hard failure into a usable cull. That is exactly what the RAF user asked Apple for.
- When the embedded preview is small (under about 3,000 px), the app should automatically decode the full RAW in the background for the current and next frames, and tell the user which bodies or settings cause it.

### Gaps
- Nothing user-reported was found for Hasselblad 3FR/FFF or Panasonic RW2 in culling apps. Searches returned nothing specific.
- No exact table was found of embedded-JPEG sizes per body (Canon R5 II, R1, Nikon Z8/Z9, Fuji X-H2S/GFX, OM-1 II, S1R II, X2D). This needs a sample-file test, for example from raw.pixls.us.

## 10. Explicit "I wish an app did X" requests (consolidated)

### Takeaway
The asks that recur most often, across sources, without a satisfying mainstream answer as of Nov 2026:

### Cited Findings
- Rank a burst by sharpness inside a chosen or per-frame region, ideally the AF point or eye — [Adobe 666325](https://community.adobe.com/feature-requests-676/p-find-the-sharpest-photo-based-on-the-eyes-666325); [Adobe 1643207](https://community.adobe.com/feature-requests-676/p-side-by-side-sharpness-comparison-for-photo-culling-1643207)
- AF-point overlay on all brands, with zoom-to-AF — [FastRawViewer](https://www.fastrawviewer.com/node/826); [photools](https://photools.com/community/index.php?msg=27370)
- Edge-detection / focus-peaking overlay, side by side, with adjustable sensitivity — [Adobe 1643207](https://community.adobe.com/feature-requests-676/p-side-by-side-sharpness-comparison-for-photo-culling-1643207); [Adobe 666325](https://community.adobe.com/feature-requests-676/p-find-the-sharpest-photo-based-on-the-eyes-666325)
- AI that proposes without changing my flags, is stable between runs, runs only on demand, and can be switched off permanently — [Adobe feedback thread](https://community.adobe.com/questions-675/p-assisted-culling-feedback-thread-lrc-1627467/index3.html)
- Wildlife edge cases: bird facing away, head turned, clipped by the frame edge — [BCG BurstPick](https://bcgforums.com/threads/burstpick-1-0-release.55925/)
- Bulk reject and delete to Trash in few steps, with undo — [TalkPhotography](https://www.talkphotography.co.uk/threads/facecull-anyone-want-to-test-a-fast-culling-app-for-events.776973/)
- Direct 1–5 rating buttons and relative +/- rating on controller dials — [ishootshows](https://ishootshows.com/tourbox-neo-review-for-photographers/)
- Preserve in-camera ratings from both cards and both RAW and JPEG, including video — [Adobe 5D IV](https://community.adobe.com/questions-675/5d-mk4-star-rating-not-showing-in-lightroom-985735)
- Show at least the embedded JPEG for RAWs the OS can't decode yet — [Apple Discussions](https://discussions.apple.com/thread/255613945)
- Color labels that round-trip with Capture One — [Capture One](https://support.captureone.com/hc/de/community/posts/360009386958-Metadata-sync)
- A per-folder sharpness overlay pre-generated like 1:1 previews, scaled for high-MP files — [Adobe 666325](https://community.adobe.com/feature-requests-676/p-find-the-sharpest-photo-based-on-the-eyes-666325)
- File size as a sortable column, as a crude blur proxy (a 2012 suggestion, with a caveat from another user) — [Adobe 666325](https://community.adobe.com/feature-requests-676/p-find-the-sharpest-photo-based-on-the-eyes-666325)

### Inferences
- Five or more new indie cullers in 2025–2026 (BurstPick, Wildlife Engine, Tack, Picturesque, FaceCull, plus a BCG alpha) are all chasing the same gap: a fast, local, Photo Mechanic-class viewer with burst sharpness ranking and AF/subject awareness across brands. None appears to combine all of this with reliable metadata yet.

### Gaps
- Reddit, DPReview and YouTube comment sentiment could not be accessed or quantified in this pass. Frequency labels are therefore based on forum and vendor-board evidence only. Aftershoot and Narrative feedback boards were not reachable through search.
