
# 📘 How to Enable Chinese Text in OpenCV (with Example)

OpenCV’s built-in `cv2.putText()` does **not** support Chinese characters because it only uses a limited Hershey font.  
To display Chinese text, you must:

1. Load the image using OpenCV
    
2. Convert it to a PIL image
    
3. Use a TrueType Chinese font (`.ttf`) to draw Chinese text
    
4. Convert back to an OpenCV `numpy` array
    
5. Continue using OpenCV normally
    

---

# ✅ Requirements

Install Pillow (if not already installed):

```bash
pip install pillow
```

Prepare a font that supports Chinese, such as:

- `SimHei.ttf` (黑体)
    
- `SimSun.ttf` (宋体)
    
- `NotoSansCJK-Regular.ttc` (Google Noto font)
    

Place the font file in the same directory or specify a full path.

---

# ✅ Full Example Code

```python
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# --- Load image using OpenCV ---
img = cv2.imread("test.jpg")

# Convert cv2 image (BGR) to PIL image (RGB)
img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# Create draw object
draw = ImageDraw.Draw(img_pil)

# Load a Chinese font file
font = ImageFont.truetype("SimHei.ttf", 40)

# Text to draw
text = "你好，OpenCV！"

# Draw Chinese text
draw.text((50, 50), text, font=font, fill=(255, 0, 0))  # red text

# Convert back to OpenCV (BGR)
img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

# Display
cv2.imshow("Image with Chinese", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# ✅ Explanation

### Why OpenCV cannot display Chinese

OpenCV uses **Hershey vector fonts** which only support ASCII characters.  
Any Chinese characters will appear as:

- empty boxes
    
- question marks
    
- nothing displayed
    

### Why PIL works

Pillow supports any `.ttf` or `.ttc` TrueType font, so it can accurately render:

- Chinese
    
- Japanese
    
- Korean
    
- Emoji
    
- Any Unicode characters
    

---

# 📌 Notes

- The font file _must_ support Chinese characters.
    
- If colors look wrong (red ↔ blue), it’s because OpenCV uses **BGR**, PIL uses **RGB**.
    
- For real-time webcam overlay, you can repeat the PIL conversion inside your loop.
    

---

# 📘 Quick Reference

|Task|Method|
|---|---|
|Display English text only|`cv2.putText()`|
|Display Chinese text|Use Pillow (`ImageDraw.text`)|
|Fonts needed|`.ttf` or `.ttc` that supports Chinese|
|Color mismatch|Convert between BGR ↔ RGB|
