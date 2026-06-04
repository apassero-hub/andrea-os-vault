---
title: "Velocità motori Smart Controller"
created: 2025-06-01
updated: 2025-06-01
model: gpt-4o
messages: 4
source: chatgpt-import
tags: []
---

# Velocità motori Smart Controller

> Importato da ChatGPT export · 4 messaggi · gpt-4o · 2025-06-01

## 🧑 User

posso vedere la velocità dei motori del drone sullo smart controller dji come si vedono anche sul controller di base del mavic 2?

---

## 🤖 Assistant

No, the DJI Smart Controller does not display individual motor speeds (RPM) of the drone, unlike the standard controller for the Mavic 2 series. This limitation is due to the DJI GO 4 application used with the Smart Controller, which does not include this specific telemetry data in its interface.

The standard controller, when connected to a mobile device running the DJI GO 4 app, may provide more detailed telemetry, including motor speeds, depending on the drone model and firmware version. However, the Smart Controller's built-in display and software do not offer this level of detail.

If monitoring individual motor speeds is essential for your operations, you might consider using the standard controller with a compatible mobile device running the DJI GO 4 app. Alternatively, for more advanced telemetry requirements, exploring DJI's enterprise solutions or third-party applications that support detailed flight data analysis could be beneficial.

---

## 🧑 User

ok but how can I see if there's wind or that the drone is struggling if not by motor speed?

---

## 🤖 Assistant

Excellent question. Even without direct access to motor RPM on the DJI Smart Controller, there are still **multiple indirect indicators** that can help you understand if the drone is under wind stress or struggling:

---

### ✅ 1. **Flight Telemetry – Horizontal Speed & Attitude**
- Watch for **inconsistent horizontal speed** when flying at a fixed stick input. If you're pushing forward and the drone is slow or getting pushed off course, that’s a sign of headwind.
- Pay attention to **tilt angle** in the artificial horizon: strong winds require the drone to lean significantly to hold position or make progress, especially in GPS or Tripod modes.

---

### ✅ 2. **Battery Consumption Rate**
- Check the **battery percentage drop per minute**: unusually fast drops may indicate the motors are working harder (e.g., compensating for wind).
- If you're getting a **“high power load”** warning, it often correlates with wind resistance or elevation gain.

---

### ✅ 3. **Real-Time Wind Warnings or Flight Status Messages**
- Some DJI drones (especially later models like the Mavic 3, Air 3, and Mini 3/4) **display wind warnings** like “Strong wind. Fly with caution.”
- These appear as **status alerts** in the upper or lower telemetry area of the screen.

---

### ✅ 4. **Drone Audio & Behavior**
- If you're nearby during hover or slow movement, you may **hear motors revving irregularly** or notice the drone shifting to stabilize – this often correlates with wind gusts.
- The drone may also **"crab" sideways** while trying to maintain a forward trajectory in wind.

---

### ✅ 5. **Flight Logs (Post-Flight)**
- After the flight, using DJI Assistant or third-party tools like **Airdata UAV**, you can review:
- Actual **motor output levels** (relative, not exact RPM)
- **IMU stress**
- **Wind estimation from GPS drift vs. command input**

---

### 🔍 Optional Tip: Enable Advanced Telemetry (if available)
If your aircraft supports it, you may be able to turn on **more detailed telemetry overlays** in the app (e.g., compass, pitch/roll degrees, heading, etc.). On the Smart Controller, this is usually within:
**Settings → Display → Advanced or Telemetry Overlay**

---

If you tell me your exact drone model, I can be more specific (e.g. Mavic 2 Pro, Mavic 3, Air 2S, etc.) since capabilities differ between models.