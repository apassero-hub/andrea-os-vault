import AppKit
import CoreImage
// Converte una foto nello stile Cogne Trail: bianco e nero, contrasto morbido, grana leggera.
// Uso: swift tools/bw.swift originale.jpg uscita.jpg [larghezza]   (larghezza predefinita 1600 px)
let a = CommandLine.arguments
let src = CIImage(contentsOf: URL(fileURLWithPath: a[1]))!
let target = a.count > 3 ? Double(a[3])! : 1600
// rifila 1% per lato: alcune foto hanno un bordo chiaro
let ins = src.extent.insetBy(dx: src.extent.width * 0.01, dy: src.extent.height * 0.01)
var img = src.cropped(to: ins).transformed(by: CGAffineTransform(translationX: -ins.minX, y: -ins.minY))
img = img.applyingFilter("CILanczosScaleTransform", parameters: ["inputScale": target / ins.width, "inputAspectRatio": 1.0])
img = img.transformed(by: CGAffineTransform(translationX: -img.extent.minX, y: -img.extent.minY))
// conversione con più peso a rosso e verde: prati e roccia restano leggibili
let mix = CIVector(x: 0.38, y: 0.50, z: 0.12, w: 0)
img = img.applyingFilter("CIColorMatrix", parameters: ["inputRVector": mix, "inputGVector": mix, "inputBVector": mix])
img = img.applyingFilter("CIExposureAdjust", parameters: ["inputEV": 0.2])
img = img.applyingFilter("CIGammaAdjust", parameters: ["inputPower": 0.92])
img = img.applyingFilter("CIColorControls", parameters: ["inputContrast": 1.1, "inputSaturation": 0])
img = img.applyingFilter("CIToneCurve", parameters: ["inputPoint0": CIVector(x:0,y:0.06),"inputPoint1": CIVector(x:0.25,y:0.26),"inputPoint2": CIVector(x:0.5,y:0.5),"inputPoint3": CIVector(x:0.75,y:0.82),"inputPoint4": CIVector(x:1,y:0.97)])
let noise = CIFilter(name: "CIRandomGenerator")!.outputImage!.cropped(to: img.extent)
  .applyingFilter("CIColorMatrix", parameters: ["inputRVector": CIVector(x:0,y:1,z:0,w:0),"inputGVector": CIVector(x:0,y:1,z:0,w:0),"inputBVector": CIVector(x:0,y:1,z:0,w:0),"inputAVector": CIVector(x:0,y:0,z:0,w:0.06)])
img = noise.composited(over: img).cropped(to: img.extent)
let cg = CIContext().createCGImage(img, from: img.extent)!
try! NSBitmapImageRep(cgImage: cg).representation(using: .jpeg, properties: [.compressionFactor: 0.7])!.write(to: URL(fileURLWithPath: a[2]))
