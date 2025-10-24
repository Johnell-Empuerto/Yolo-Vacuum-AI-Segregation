import time
from adafruit_servokit import ServoKit

# Initialize PCA9685 with 16 channels
kit = ServoKit(channels=16)

# Set PWM frequency to 50Hz (standard for MG996R)
kit.servo[0].set_pulse_width_range(1000, 2000)  # 1000μs (0°), 2000μs (180°)

print("Moving servo on channel 0... Press Ctrl+C to stop.")

try:
    while True:
        kit.servo[0].angle = 0    # Move to 0 degrees
        time.sleep(1)
        kit.servo[0].angle = 90   # Move to 90 degrees
        time.sleep(1)
        kit.servo[0].angle = 180  # Move to 180 degrees
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping servo.")
    kit.servo[0].angle = None  # Stop PWM signal