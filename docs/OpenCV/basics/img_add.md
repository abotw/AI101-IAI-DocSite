
# Image Arithmetic Operations

```python
import cv2  
  
# Read images  
img_a = cv2.imread('ex.jpg')  
img_b = cv2.imread('avatar.jpg')  
  
# Simple pixel addition  
# Adds 10 to all pixel values; values above 255 will wrap around (e.g. 260 -> 4)  
img_c = img_a + 100  
  
# cv2.imshow('Original', img_a)  
cv2.imshow('After + 100', img_c)  
cv2.waitKey(0)  
  
# Add two image regions  
roi_a = img_a[50:450, 50:400]  
roi_b = img_b[50:450, 50:400]  
roi_c = roi_a + roi_b  
  
cv2.imshow('ROI Addition', roi_c)  
cv2.waitKey(0)  
  
# Safe addition using cv2.add()  
# Ensures that overflow values are clipped to 255 instead of wrapping around.  
resized_a = cv2.resize(img_a, (400, 400))  
resized_b = cv2.resize(img_b, (400, 400))  
resized_c = cv2.add(resized_a, resized_b)  
  
cv2.imshow('Using cv2.add()', resized_c)  
cv2.waitKey(0)  
  
cv2.destroyAllWindows()
```

```python
import cv2  
  
# Read and resize images  
img_a = cv2.imread('ex.jpg')  
img_b = cv2.imread('avatar.jpg')  
  
resized_a = cv2.resize(img_a, (400, 400))  
resized_b = cv2.resize(img_b, (400, 400))  
  
# Weighted addition  
weighted_img = cv2.addWeighted(resized_a, 0.5, resized_b, 0.5, 10)  
  
cv2.imshow('Weighted Addition', weighted_img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()
```

## Optimized Code

```python
"""
-------------------------------------------------------
Image Arithmetic Operations using OpenCV
-------------------------------------------------------
Demonstrates:
1. Simple pixel addition
2. Safe addition with cv2.add()
3. Weighted image blending
-------------------------------------------------------
Author: AI101
-------------------------------------------------------
"""

import cv2


def show_image(window_name: str, image):
    """Display an image until a key is pressed."""
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


def add_scalar_to_image(image, value: int):
    """
    Add a scalar value to all pixels in an image.
    Note: Overflow wraps around (e.g., 260 → 4).
    """
    return image + value


def add_image_regions(img_a, img_b, region_a, region_b):
    """
    Add two image regions directly (risk of overflow).
    """
    roi_a = img_a[region_a[0]:region_a[1], region_a[2]:region_a[3]]
    roi_b = img_b[region_b[0]:region_b[1], region_b[2]:region_b[3]]
    return roi_a + roi_b


def safe_add_images(img_a, img_b, size=(400, 400)):
    """
    Safely add two resized images using cv2.add(),
    ensuring overflow values are clipped to 255.
    """
    a_resized = cv2.resize(img_a, size)
    b_resized = cv2.resize(img_b, size)
    return cv2.add(a_resized, b_resized)


def weighted_blend(img_a, img_b, alpha=0.5, beta=0.5, gamma=10, size=(400, 400)):
    """
    Blend two images using weighted addition:
    result = α·A + β·B + γ
    """
    a_resized = cv2.resize(img_a, size)
    b_resized = cv2.resize(img_b, size)
    return cv2.addWeighted(a_resized, alpha, b_resized, beta, gamma)


def main():
    # --- Load Images ---
    img_a = cv2.imread("ex.jpg")
    img_b = cv2.imread("avatar.jpg")

    if img_a is None or img_b is None:
        print("Error: One or both image files could not be loaded.")
        return

    # --- Simple pixel addition ---
    img_plus_100 = add_scalar_to_image(img_a, 100)
    show_image("Original", img_a)
    show_image("After +100", img_plus_100)

    # --- Add two image regions (unsafe addition) ---
    roi_sum = add_image_regions(img_a, img_b, (50, 450, 50, 400), (50, 450, 50, 400))
    show_image("ROI Addition", roi_sum)

    # --- Safe addition using cv2.add() ---
    safe_sum = safe_add_images(img_a, img_b)
    show_image("cv2.add() Safe Addition", safe_sum)

    # --- Weighted image blending ---
    blended = weighted_blend(img_a, img_b, alpha=0.5, beta=0.5, gamma=10)
    show_image("Weighted Blend", blended)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
```

---

## 📘 AI101 Documentation

### **Topic:** Image Arithmetic Operations in OpenCV

#### **Overview**

Image arithmetic is a fundamental concept in computer vision. It involves pixel-wise mathematical operations on images, enabling effects such as brightness adjustment, image blending, and combining multiple image regions.

OpenCV provides efficient built-in functions to perform arithmetic operations with automatic handling of overflow and type consistency.

---

### **1. Simple Pixel Addition**

**Operation:**

```python
img_result = img + 100
```

This adds a constant value to every pixel.  
⚠️ **Caution:** When using NumPy addition, pixel values above 255 wrap around (e.g., 260 → 4).

**Use case:** quick brightness enhancement (but unsafe).

---

### **2. Safe Addition with `cv2.add()`**

**Operation:**

```python
result = cv2.add(imageA, imageB)
```

OpenCV automatically **clips overflow values** to 255, ensuring image data integrity.

**Use case:** overlaying two images safely.

---

### **3. Region Addition**

You can perform arithmetic only on specific parts (Regions of Interest, ROI):

```python
roi_a = img_a[y1:y2, x1:x2]
roi_b = img_b[y1:y2, x1:x2]
result = roi_a + roi_b
```

**Use case:** combining local patches, partial overlays.

---

### **4. Weighted Image Blending**

**Formula:**  
[  
\text{result} = \alpha \cdot A + \beta \cdot B + \gamma  
]

**Implementation:**

```python
result = cv2.addWeighted(imageA, 0.5, imageB, 0.5, 10)
```

This produces a smooth, visually pleasing blend between two images — commonly used in crossfades, transparency effects, or HDR image composition.

---

### **5. Key Differences**

|Method|Handles Overflow|Adjustable Weights|Typical Use|
|---|---|---|---|
|`img + value`|❌ Wraps around|❌|Quick brightness change|
|`cv2.add()`|✅ Clipped at 255|❌|Safe image addition|
|`cv2.addWeighted()`|✅ Clipped at 255|✅|Image blending|

---

### **Example Output Preview**

|Operation|Result Description|
|---|---|
|**After +100**|Brighter image (unsafe overflow)|
|**ROI Addition**|Local sum of two cropped areas|
|**cv2.add() Safe Addition**|Combined image without overflow artifacts|
|**Weighted Blend**|Smooth composite between both inputs|

---

### **Best Practices**

- Always check if images are loaded successfully.
    
- Use `cv2.add()` or `cv2.addWeighted()` for production-level image arithmetic.
    
- Resize images to the same size before combining.
    
- Use small gamma values (e.g. `+10`) for natural-looking brightness adjustments.
    

---

Would you like me to make this **AI101 doc version** include a **Quick Reference Table + Code Snippets** (like the “Example + Output” section in your previous AI101 docs)? That version fits perfectly for your documentation site.

### 🔧 Improvements Made

- Cleaned up redundant reads and redefinitions.
    
- Added clear variable naming (`roi_a`, `roi_b`, `a_resized`).
    
- Included comments about overflow vs. clipping behavior.
    
- Added consistent window names for easier comparison.
    

---

## 🧾 Quick Reference: Image Arithmetic in OpenCV

### 🔹 1. Pixel Addition

You can directly add a constant value to an image:

```python
img_new = img + 10
```

⚠️ **NumPy addition wraps around** when the result exceeds 255.  
Example: `250 + 10 = 4`.

---

### 🔹 2. Image Addition (NumPy)

```python
result = img1 + img2
```

Both images must be of the same **size and data type**.  
Overflow values **wrap around** — so `255 + 10 → 9`.

---

### 🔹 3. Safe Addition (`cv2.add`)

```python
result = cv2.add(img1, img2)
```

- Values are **clipped at 255** instead of wrapping.  
    Example: `250 + 10 = 255`
    
- Recommended for **image blending** or **brightness adjustment**.
    

---

### 🔹 4. Weighted Addition (Image Blending)

Combine two images with given weights:

```python
blend = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
```

Formula:  
[  
\text{output} = img1 \times \alpha + img2 \times \beta + \gamma  
]

---

### 📚 Summary

|Operation|Function|Overflow Behavior|Use Case|
|---|---|---|---|
|`a + 10`|NumPy add|Wraps (260→4)|Quick pixel test|
|`a + b`|NumPy add|Wraps|Simple math ops|
|`cv2.add(a, b)`|OpenCV add|Clipped (260→255)|Safe blending|
|`cv2.addWeighted()`|Weighted add|Clipped|Image overlay / transparency|
