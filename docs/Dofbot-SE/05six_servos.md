---
title: 05. Six Servos
---

# Controlling All Six Servos Simultaneously

## 1. API Overview

To control all six bus servos of the robotic arm at once, use the following API:

### **`Arm_serial_servo_write6(S1, S2, S3, S4, S5, S6, time)`**

**Function:**  
Controls all six servos simultaneously, moving each one to its specified target angle.

**Parameters:**

|Parameter|Description|Range|
|---|---|---|
|**S1**|Servo 1 target angle|0–180°|
|**S2**|Servo 2 target angle|0–180°|
|**S3**|Servo 3 target angle|0–180°|
|**S4**|Servo 4 target angle|0–180°|
|**S5**|Servo 5 target angle|0–270°|
|**S6**|Servo 6 target angle|0–180°|
|**time**|Duration (ms) — time for all servos to complete movement|≥0|

**Notes:**

- The smaller the **time** value, the **faster** the movement.
    
- Setting **time = 0** makes the servos move **at maximum speed**.
    
- The function does **not return** any value.
    

---

## 2. Example Code

**File path:**  
`/home/yahboom/Dofbot/3.ctrl_Arm/5.ctrl_all.ipynb`

```python
#!/usr/bin/env python3
# coding=utf-8

import time
from Arm_Lib import Arm_Device

# Create the Arm device object
Arm = Arm_Device()
time.sleep(0.1)

# Function to control all six servos simultaneously
def ctrl_all_servos(angle, s_time=500):
    """
    Move all six servos to specific angles.
    For demonstration, servo 2 moves in the opposite direction of servo 1.
    """
    Arm.Arm_serial_servo_write6(
        angle,             # Servo 1
        180 - angle,       # Servo 2 (mirror motion)
        angle,             # Servo 3
        angle,             # Servo 4
        angle,             # Servo 5
        angle,             # Servo 6
        s_time             # Duration (ms)
    )
    time.sleep(s_time / 1000.0)

def main():
    direction = 1
    angle = 90

    # Reset all servos to center position
    Arm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 90, 500)
    time.sleep(1)

    # Loop to continuously move all servos back and forth
    while True:
        if direction == 1:
            angle += 1
            if angle >= 180:
                direction = 0
        else:
            angle -= 1
            if angle <= 0:
                direction = 1

        ctrl_all_servos(angle, 10)
        time.sleep(0.01)  # Slight delay to control movement smoothness

try:
    main()
except KeyboardInterrupt:
    print("Program closed by user.")
    pass

# Release the Arm device resource
del Arm
```

---

## 3. How to Run in JupyterLab

1. Open **JupyterLab** and navigate to:
    
    ```
    /home/yahboom/Dofbot/3.ctrl_Arm/5.ctrl_all.ipynb
    ```
    
2. Click **“Run All”** in the toolbar to execute the entire notebook.
    
3. The robotic arm’s six servos will **move simultaneously**, changing the arm’s posture continuously.
    
    - The motion alternates between 0° and 180°, creating a smooth oscillating effect.
        
4. To stop the motion, click the **“Stop”** button on the JupyterLab toolbar.
    

---

## 4. Notes

- Use this function to perform **synchronized, multi-joint movements** for coordinated robotic gestures.
    
- Adjust the **`time`** parameter to balance between speed and stability.
    
- Avoid setting extremely fast speeds for large angle movements — this can cause vibration or instability.
    
- Always reset the arm to a neutral position (90°, 90°, 90°, 90°, 90°, 90°) before complex motions.
    
- After the script finishes, use **`del Arm`** to safely release hardware control.
    

---

## 5. Example Applications

- Coordinated arm movement demonstrations
    
- Gesture playback or motion recording systems
    
- Smooth transitions between saved postures
    
- Basic testing of servo synchronization and performance
    

