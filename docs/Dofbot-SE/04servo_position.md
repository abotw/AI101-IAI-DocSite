---
title: 04. Servo Position
---

# 6.4 Reading the Current Servo Position

## 1. API Overview

You can read the current angle (position) of a single **bus servo motor** using the following API:

### **`Arm_serial_servo_read(id)`**

**Function:**  
Reads the current angle value of the servo motor with the specified ID.

**Parameters:**

- **`id`** _(int)_ — The ID number of the servo motor to read.
    
    - Range: **1–6**
        
    - Each ID corresponds to one servo motor, numbered from **bottom (1)** to **top (6)**.
        

**Return value:**

- Returns the **current angle** of the specified servo motor.
    
- For **servo ID 5**, the valid range is **0–270°**.
    
- For all other servos, the range is **0–180°**.
    

---

## 2. Example Code

**File path:**  
`/home/yahboom/Dofbot/3.ctrl_Arm/4.ctrl_servo.ipynb`

```python
#!/usr/bin/env python3
# coding=utf-8

import time
from Arm_Lib import Arm_Device

# Create the Arm device object
Arm = Arm_Device()
time.sleep(0.1)

# Example 1: Continuously read and print the angles of all six servos
def main():
    while True:
        for i in range(6):
            angle_value = Arm.Arm_serial_servo_read(i + 1)
            print(f"Servo {i + 1} angle: {angle_value}")
            time.sleep(0.01)
        print("End of line!\n")
        time.sleep(0.5)

try:
    main()
except KeyboardInterrupt:
    print("Program closed by user.")
    pass

# Example 2: Move one servo and then read its angle
servo_id = 6
target_angle = 150
Arm.Arm_serial_servo_write(servo_id, target_angle, 500)
time.sleep(1)

current_angle = Arm.Arm_serial_servo_read(servo_id)
print(f"Servo {servo_id} current angle: {current_angle}")

time.sleep(0.5)

# Release the Arm device resource
del Arm
```

---

## 3. How to Run in JupyterLab

1. Open **JupyterLab** and navigate to:
    
    ```
    /home/yahboom/Dofbot/3.ctrl_Arm/4.ctrl_servo.ipynb
    ```
    
2. Click **“Run All”** in the toolbar to execute the entire notebook.
    
3. The notebook will continuously **print the current angles** of all six servos in real time.
    
4. It will also move the servo with **ID = 6** to **150°**, then display its updated angle.
    
5. To stop the program, click the **“Stop”** button in the JupyterLab toolbar.
    

---

## 4. Notes

- Servo angle readings update dynamically, allowing you to monitor the arm’s posture in real time.
    
- Frequent reads (short delays) may increase CPU load; adjust the interval (`time.sleep()`) as needed.
    
- The returned angle values are measured from the servo’s internal position sensor.
    
- Always ensure that the servo ID is valid (1–6) before calling this function.
    
- Use **`del Arm`** at the end of the script to safely close the device connection.
    
