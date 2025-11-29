---
title: 01. RGB
---

# 🌈 Control the RGB Light on Dofbot

## 1. Overview

The Dofbot expansion board supports controlling servos, an RGB LED, and a buzzer.  
The low-level drivers are provided as a Python library called **Arm_Lib**, which can be installed from the `Dofbot.zip` package.

After extraction and installation:

```bash
unzip Dofbot.zip
cd Dofbot/0.py_install && sudo python3 setup.py install
```

If you see output like:

```
Arm_Lib = x.x.x installed successfully
```

then the library is ready to use.

---

## 2. API Reference

**Function:**

```python
Arm.Arm_RGB_set(R, G, B)
```

**Description:**  
Sets the RGB LED color on the Dofbot expansion board.

**Parameters:**

|Parameter|Type|Range|Description|
|---|---|---|---|
|`R`|int|0–255|Red brightness|
|`G`|int|0–255|Green brightness|
|`B`|int|0–255|Blue brightness|

**Return:** None

---

## 3. Example Code

**File Path:** `/home/yahboom/Dofbot/3.ctrl_Arm/1.rgb.ipynb`

This script continuously cycles the RGB LED through red, green, and blue colors at 0.5-second intervals.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------------------
Control RGB LED on Dofbot Expansion Board
----------------------------------------------------------
This script cycles the onboard RGB LED through red, green,
and blue colors in a loop. Press Ctrl+C to stop.
----------------------------------------------------------
"""

import time
from Arm_Lib import Arm_Device

# Initialize the robotic arm device
arm = Arm_Device()
time.sleep(0.1)  # Short delay for initialization

def cycle_rgb_lights():
    """Continuously cycle the RGB LED through red, green, and blue."""
    while True:
        arm.Arm_RGB_set(50, 0, 0)   # Red
        time.sleep(0.5)
        arm.Arm_RGB_set(0, 50, 0)   # Green
        time.sleep(0.5)
        arm.Arm_RGB_set(0, 0, 50)   # Blue
        time.sleep(0.5)
        print("RGB cycle complete.")

try:
    cycle_rgb_lights()
except KeyboardInterrupt:
    # Release the Arm device safely on exit
    del arm
    print("Program terminated by user.")
```

---

## 4. Running the Code in JupyterLab

1. Open **JupyterLab**.
    
2. Navigate to `/home/yahboom/Dofbot/3.ctrl_Arm/1.rgb.ipynb`.
    
3. Click **Run All Cells** in the toolbar.
    
4. Observe the RGB LED on the Dofbot board cycling every 0.5 seconds:  
    🔴 → 🟢 → 🔵 → (repeat)
    

To **stop the program**, click the **Stop (■)** button in JupyterLab’s toolbar.

---

## 5. Improvements in This Version

|Area|Original|Improved|
|---|---|---|
|**Indentation**|Misaligned `while True:` loop|Proper indentation|
|**Naming**|`Arm`|Changed to lowercase `arm` for Python convention|
|**Function design**|Inline infinite loop|Wrapped into `cycle_rgb_lights()`|
|**Comments**|Sparse|Added clear, structured comments|
|**Docstring**|None|Added a full header docstring|
|**Exception handling**|Present but minimal|Clear user feedback and safe cleanup|
|**Print statements**|“END OF LINE!”|Replaced with meaningful output|

---

## 6. Learning Notes

- You can adjust the brightness or mix colors by changing RGB values.  
    Example:
    
    ```python
    arm.Arm_RGB_set(30, 30, 0)  # Yellow (Red + Green)
    ```
    
- To turn off the LED:
    
    ```python
    arm.Arm_RGB_set(0, 0, 0)
    ```
    
- The color update delay can be customized by changing the `time.sleep()` interval.
    

---

## ✅ Summary

This improved version follows **Pythonic style**, improves **readability**, and is more **maintainable**.  
It can serve as a template for other Dofbot control scripts — such as controlling servos or the buzzer.
