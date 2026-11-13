import AVFoundation
import AppKit
// apri <video> <prefisso>: dice se macOS lo apre, la durata, e salva tre fotogrammi
let url = URL(fileURLWithPath: CommandLine.arguments[1]); let pre = CommandLine.arguments[2]
let asset = AVURLAsset(url: url)
let sem = DispatchSemaphore(value: 0)
Task {
    do {
        let playable = try await asset.load(.isPlayable); let dur = try await asset.load(.duration)
        let tr = try await asset.loadTracks(withMediaType: .video)
        print("\(url.lastPathComponent): apribile=\(playable) durata=\(String(format: "%.2f", dur.seconds)) s tracce video=\(tr.count)")
        let gen = AVAssetImageGenerator(asset: asset); gen.requestedTimeToleranceBefore = .zero; gen.requestedTimeToleranceAfter = .zero
        for s in [0.5, 3.3, 6.6] {
            let (img, _) = try await gen.image(at: CMTime(seconds: s, preferredTimescale: 24000))
            let rep = NSBitmapImageRep(cgImage: img); try rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: "\(pre)_\(s).png"))
        }
    } catch { print("\(url.lastPathComponent): NON si apre (\(error.localizedDescription))") }
    sem.signal()
}
sem.wait()
