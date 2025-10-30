Here’s your **fully updated README.md**, with the new “System Auto-Run + Delay Logic” section added — and clearly stating that **the vacuum must be turned on manually** 👇

---

````markdown
# 🧠 Vacuum AI — YOLOv8n on Raspberry Pi

This project demonstrates how to use **YOLOv8n** for **AI-powered trash segregation** on a **Raspberry Pi** with a **servo-controlled robotic arm**.  
The system detects compostable and non-compostable items using a camera and automatically sorts them into the correct bins.

---

## 📸 Test the Camera on Raspberry Pi

```bash
export DISPLAY=:0
rpicam-hello -t 0
````

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
However, the **vacuum motor must be turned on manually** after detection.

1. **Startup Process:**

   * After powering on, the Raspberry Pi will load the camera and YOLO model automatically.
   * This process usually takes **20–30 seconds** before the video and detection begin.

2. **Detection Process:**

   * When the system detects a compostable or non-compostable item, it waits for about **20 seconds** before moving the servo.
   * This short delay helps the AI confirm the object properly before sorting.

3. **Manual Vacuum Activation:**

   * Once you see the detection on screen, **manually switch on the vacuum** to start the suction and sorting process.
   * The vacuum runs based on your control — the AI only handles **servo movement** (left/right for sorting).

4. **Idle State:**

   * If no object is detected, the AI system remains idle, and the vacuum stays off until you decide to run it.

5. **Manual Restart (Optional):**

   ```bash
   sudo systemctl restart yolo.service
   ```

6. **Check Logs (Optional):**

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

```

