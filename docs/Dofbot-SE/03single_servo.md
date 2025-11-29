---
title: 03. Single Servo
---

# Control a Single Servo Motor

## 1. API Overview

The robotic arm’s single **bus servo motor** can be controlled using the following API:

### **`Arm_serial_servo_write(id, angle, time)`**

**Function:**  
Controls a specific servo motor to rotate to a given angle.

**Parameters:**

- **`id`** _(int)_ — The ID number of the servo motor to control.
    
    - Range: **1–6**
        
    - Each ID corresponds to one servo motor:
        
        - ID 1 = bottom servo
            
        - ID 6 = top servo
            
- **`angle`** _(int)_ — The target angle for the servo motor.
    
    - For **most servos (ID 1–6, except ID 5)**: valid range is **0–180°**
        
    - For **servo ID 5**: valid range is **0–270°**
        
- **`time`** _(int)_ — The duration of movement in milliseconds.
    
    - Smaller values → faster movement.
        
    - If `time = 0`, the servo moves **at maximum speed**.
        

**Return value:**  
None

---

## 2. Example Code

**File path:**  
`/home/yahboom/Dofbot/3.ctrl_Arm/3.ctrl_servo.ipynb`

```python
#!/usr/bin/env python3
# coding=utf-8

import time
from Arm_Lib import Arm_Device

# Create the Arm device object
Arm = Arm_Device()
time.sleep(0.1)

# Example 1: Move a single servo (ID = 6) to 90 degrees within 500 ms
servo_id = 6
Arm.Arm_serial_servo_write(servo_id, 90, 500)
time.sleep(1)

# Example 2: Continuously move the same servo between different angles
def main():
    while True:
        Arm.Arm_serial_servo_write(servo_id, 120, 500)
        time.sleep(1)
        Arm.Arm_serial_servo_write(servo_id, 50, 500)
        time.sleep(1)
        Arm.Arm_serial_servo_write(servo_id, 120, 500)
        time.sleep(1)
        Arm.Arm_serial_servo_write(servo_id, 180, 500)
        time.sleep(1)

try:
    main()
except KeyboardInterrupt:
    print("Program closed by user.")

# Release the Arm device resource
del Arm
```

---

## 3. How to Run in JupyterLab

1. Open **JupyterLab** and navigate to:
    
    ```
    /home/yahboom/Dofbot/3.ctrl_Arm/3.ctrl_servo.ipynb
    ```
    
2. Click **“Run All”** in the toolbar to execute the entire notebook.
    
3. You will see the **claw (top servo, ID=6)** continuously changing its angle.
    
    - It moves between 50°, 120°, and 180° repeatedly.
        
4. To stop the program, click the **“Stop”** button in the JupyterLab toolbar.
    

---

## 4. Notes

- The **movement duration** (`time`) affects speed: shorter times make the servo rotate faster.
    
- Use reasonable `angle` and `time` values to prevent excessive torque or vibration.
    
- Always use **`del Arm`** after your program finishes to safely release the hardware interface.
    
- If the servo doesn’t move:
    
    - Check the power supply and connections.
        
    - Make sure the servo ID is within the correct range (1–6).
        
