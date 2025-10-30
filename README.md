Perfect — here’s your **updated README** with your new section (“System Auto-Run + Delay Logic”) inserted naturally near the end, keeping the flow clear and human-readable 👇

---

# 🧠 Vacuum AI — YOLOv8n on Raspberry Pi

This project demonstrates how to use **YOLOv8n** for **AI-powered trash segregation** on a **Raspberry Pi** with a **servo-controlled robotic arm**.
The system detects compostable and non-compostable items using a camera and automatically sorts them into the correct bins.

---

## 📸 Test the Camera on Raspberry Pi

```bash
export DISPLAY=:0
rpicam-hello -t 0
```

---

## ⚙️ Install Dependencies and Create a Folder

```bash
sudo apt update && sudo apt upgrade -y
mkdir yolo  # Create a project folder
cd yolo
python3 -m venv --system-site-packages venv  # Create a virtual environment
source venv/bin/activate  # Activate the virtual environment
```

---

## 🤖 Install YOLOv8 for Raspberry Pi

```bash
cd yolo
source venv/bin/activate  # Activate the virtual environment
pip install ultralytics ncnn
```

---

## 📦 Download a YOLOv8n Model (from COCO)

```bash
yolo detect predict model=yolov8n.pt
```

This command downloads and opens the **YOLOv8n** model.

---

## 🔄 Export YOLO to NCNN Format

```bash
yolo export model=yolov8n.pt format=ncnn
```

---

## 💻 Download the Object Detection Code

(Credits to [ejtech.io](https://ejtech.io))

```bash
wget https://ejtech.io/code/yolo_detect.py
```

---

## ▶️ Run YOLO Detection

```bash
python yolo_detect.py --model=yolov8n_ncnn_model --source=picamera0 --resolution=640x480
```

---

## 🧩 For the Vacuum AI Project (Custom Model)

Download your **custom `best.pt` model** from this GitHub repository, then:

```bash
cd yolo
source venv/bin/activate
yolo export model=best.pt format=ncnn
python yolo_detect.py --model=best_ncnn_model --source=picamera0 --resolution=640x480
```

---

## ⚡ Connect Hardware

Follow the wiring diagram from this repository to connect:

* **PCA9685 module** → **Raspberry Pi**
* **Servo motor** → **PCA9685 module**

---

## 🚀 Run the Vacuum AI Servo Control

When a compostable item is detected, the arm tilts **left**.
When a non-compostable item is detected, it tilts **right** — sorting trash into the correct bin.

```bash
python yolo_servo.py --model=best_ncnn_model --source=picamera0 --resolution=640x480
```

---

## 🔁 System Auto-Run + Delay Logic

The YOLO system can automatically start when the Raspberry Pi boots up.

1. **Startup Process:**

   * After powering on, the system loads the camera and YOLO model automatically.
   * This process usually takes **20–30 seconds** before the video and detections appear.

2. **Detection and Action:**

   * Once the object is detected, the system waits around **20 seconds**.
   * This short pause allows the AI to confirm what it saw.
   * After the delay, the **vacuum motor turns ON** to suck and sort the item.

3. **Idle State:**

   * If there’s no object, the vacuum stays **off**.
   * When a new object appears, the same 20-second check happens again before the vacuum activates.

4. **Manual Restart (Optional):**
   If you ever need to restart the service manually:

   ```bash
   sudo systemctl restart yolo.service
   ```

5. **Check Logs (Optional):**
   To view real-time logs or AI detections:

   ```bash
   sudo journalctl -u yolo.service -f
   ```

---

## 📂 Repository Contents

```
├── Diagram.png
├── Diagram.xlsx
├── Instruction.txt
├── yolo_detects.py
├── yolo_servo.py
├── servo_test.py
├── custom model vacuum AI/
└── yolo models/
```

---

## 🙌 Credits

* **YOLOv8** by [Ultralytics](https://github.com/ultralytics)
* **Object detection example** from [ejtech.io](https://ejtech.io)
* **Project by:** [Johnell Empuerto](https://github.com/Johnell-Empuerto)

---

### 🧾 License

This project is open-source and free to use for educational and research purposes.

---


