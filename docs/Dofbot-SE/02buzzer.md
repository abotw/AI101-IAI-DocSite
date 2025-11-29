---
title: 02. Buzzer
---

# 6.2 Buzzer Control

## 1. API Overview

The buzzer on the robotic arm expansion board can be controlled using the following APIs:

### **`Arm_Buzzer_On(delay=255)`**

**Function:**  
Activates (turns on) the buzzer.

**Parameters:**

- **`delay`** _(int, optional)_ — Defines how long the buzzer should sound.
    
    - Range: **1–50**
        
    - Each unit represents **100 milliseconds**.
        
    - For example:
        
        - `delay=1` → 100 ms
            
        - `delay=2` → 200 ms
            
        - `delay=50` → 5 seconds (maximum)
            
    - If `delay` is **not provided** or set to **255**, the buzzer will **keep buzzing continuously** until it is manually turned off.
        

**Return value:** None

---

### **`Arm_Buzzer_Off()`**

**Function:**  
Turns off the buzzer immediately.

**Parameters:**  
None

**Return value:**  
None

---

## 2. Example Code

**File path:**  
`/home/yahboom/Dofbot/3.ctrl_Arm/2.beep.ipynb`

```python
#!/usr/bin/env python3
# coding=utf-8
import time
from Arm_Lib import Arm_Device

# Create an Arm_Device object
Arm = Arm_Device()
time.sleep(0.1)

# The buzzer will sound automatically for 100 ms, then stop
b_time = 1
Arm.Arm_Buzzer_On(b_time)
time.sleep(1)

# The buzzer will sound for 300 ms, then stop
b_time = 3
Arm.Arm_Buzzer_On(b_time)
time.sleep(1)

# The buzzer will sound continuously
Arm.Arm_Buzzer_On()
time.sleep(1)

# Turn off the buzzer manually
Arm.Arm_Buzzer_Off()
time.sleep(1)

# Release the Arm object
del Arm
```

---

## 3. How to Run in JupyterLab

1. Open JupyterLab and navigate to the file:
    
    ```
    /home/yahboom/Dofbot/3.ctrl_Arm/2.beep.ipynb
    ```
    
2. Click the **“Run All”** button on the toolbar to execute the entire notebook.
    
3. You will hear the buzzer **beep three times**:
    
    - The first beep lasts about 100 ms.
        
    - The second beep lasts longer (300 ms).
        
    - The third beep continues until manually turned off.
        
4. Once execution finishes, the notebook will exit automatically.
    

---

## 4. Notes

- The buzzer delay time is automatically handled by the API, so there is no need to add manual timing for automatic stop.
    
- Always call **`Arm_Buzzer_Off()`** after continuous mode to avoid prolonged buzzing.
    
- Use **`del Arm`** at the end of the program to properly release device resources.
    
