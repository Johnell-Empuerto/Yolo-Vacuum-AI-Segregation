import sys
import time
import numpy as np
from ultralytics import YOLO
from picamera2 import Picamera2

# Load the model
model = YOLO("yolov8n_ncnn_model")  # Adjust path if needed

# Since your model has only two classes: 'Compostable' and 'Non-Compostable'
# We assume class 0 is 'Compostable' and class 1 is 'Non-Compostable' (check model.names if needed)
compostable_class_name = 'Compostable'  # Exact name from your model

# Initialize Picamera2
cap = Picamera2()
cap.configure(cap.create_video_configuration(main={"format": 'RGB888', "size": (640, 480)}))  # Adjust resolution as needed
cap.start()

# FPS tracking
avg_frame_rate = 0
frame_rate_buffer = []
fps_avg_len = 200
min_thresh = 0.5  # Confidence threshold

print("Running headless YOLO detection. Press Ctrl+C to quit.")

try:
    while True:
        t_start = time.perf_counter()

        # Capture frame
        frame = cap.capture_array()
        if frame is None:
            print("Failed to grab frame")
            break

        # Run inference
        results = model(frame, imgsz=320, conf=min_thresh, half=True, verbose=False)

        # Check for compostable items
        is_compostable = False
        detections = results[0].boxes
        for i in range(len(detections)):
            classidx = int(detections[i].cls.item())
            classname = model.names[classidx]
            conf = detections[i].conf.item()
            if conf > min_thresh and classname == compostable_class_name:
                is_compostable = True
                print(f"Detected {classname} ({conf:.2f})")
            else:
                print(f"Detected {classname} ({conf:.2f})")  # Optional: Print non-compostable too

        # Print result
        print(f"Compostable: {'Yes' if is_compostable else 'No'}")

        # FPS calc
        t_stop = time.perf_counter()
        frame_rate_calc = 1 / (t_stop - t_start)
        if len(frame_rate_buffer) >= fps_avg_len:
            frame_rate_buffer.pop(0)
        frame_rate_buffer.append(frame_rate_calc)
        avg_frame_rate = np.mean(frame_rate_buffer)
        print(f"FPS: {avg_frame_rate:.2f}")

except KeyboardInterrupt:
    print("Exiting...")

# Cleanup
print(f"Average FPS: {avg_frame_rate:.2f}")
cap.stop()