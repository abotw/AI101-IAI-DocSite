---
tags:
  - image
---

# Image Operations in OpenCV

This section introduces several essential image operations in OpenCV, including:

- Modifying image pixels
    
- Combining images
    
- Resizing images
    

All examples are based on **NumPy** and **OpenCV** (`cv2`).

---

## 🧠 1. Modifying Image Pixels

In OpenCV, images are stored as NumPy arrays — so you can directly access and modify their pixel values using slicing.

```python
import cv2  
import numpy as np  
  
# Read the image  
img = cv2.imread('ex.jpg')  
  
# Replace a region with random color values  
img[0:200, 0:200] = np.random.randint(0, 256, (200, 200, 3))  
  
cv2.imshow('Mosaic', img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()
```

### Explanation

|Code|Description|
|---|---|
|`np.random.randint(0, 256, (100, 100, 3))`|Generates a random RGB color matrix of size 100×100.|
|`a[100:200, 200:300] = ...`|Replaces that area in the original image with the random colors.|
|`cv2.imshow()`|Displays the modified image.|

> ⚠️ **Note:** The replacement area and the array size must match exactly — otherwise, NumPy will raise a shape error.

---

## 🧩 2. Combining Two Images

We can also **paste one image onto another** — for example, inserting a smaller image into a specific region of a larger one.

```python
import cv2  
  
img_a = cv2.imread('ex.jpg')        # Background image  
img_b = cv2.imread('avatar.jpg')    # Foreground image  
  
# Define a region in the background and copy the smaller image into it  
img_a[200:600, 200:600] = img_b[100:500, 200:600]  
  
cv2.imshow('Image A', img_a)  
cv2.imshow('Image B', img_b)  
cv2.waitKey(0)  
cv2.destroyAllWindows()
```

### Explanation

|Concept|Description|
|---|---|
|**Image overlay**|A smaller image `b` is copied into a region of `a`.|
|**Same size requirement**|The region of `a` and the part of `b` must have the same dimensions.|
|**Practical use**|This technique can be used for watermarking, object blending, or image mosaics.|

---

## 🖼️ 3. Resizing Images with `cv2.resize`

`cv2.resize()` is used to scale images up or down.  
It accepts several parameters to control size and scaling behavior.

```python
import cv2  
  
img = cv2.imread('ex.jpg')  
  
# Resize the image to a fixed width and height  
resized_img = cv2.resize(img, (100, 200))  
# resized_img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)  
  
cv2.imshow('Image', img)  
cv2.imshow('Resized Image', resized_img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()
```

### Parameters

| Parameter       | Description                                                                             |
| --------------- | --------------------------------------------------------------------------------------- |
| `src`           | Source image (NumPy array).                                                             |
| `dsize`         | Target size (width, height). If `None`, scaling factors `fx` and `fy` are used instead. |
| **`fx`, `fy`**  | **Scaling factors for the x and y axes.**                                               |
| `interpolation` | (Optional) Interpolation method, e.g., `cv2.INTER_LINEAR`, `cv2.INTER_AREA`, etc.       |

Example with scale factors:

```python
a_new = cv2.resize(a, dsize=None, fx=0.5, fy=0.5)
```

---

## ⚙️ Practical Notes

- **Upscaling vs Downscaling:**
    
    - For **shrinking**, `cv2.INTER_AREA` works best.
        
    - For **enlarging**, use `cv2.INTER_LINEAR` or `cv2.INTER_CUBIC`.
        
- **Aspect ratio:**  
    Always keep the same aspect ratio unless a specific deformation is desired.
    
- **Performance:**  
    Resizing large images repeatedly can be expensive; cache or precompute resized versions if possible.
    

---

## ✅ Summary

|Operation|Function|Description|
|---|---|---|
|Modify pixels|NumPy slicing|Change specific image areas|
|Combine images|Image assignment|Paste one image into another|
|Resize image|`cv2.resize()`|Scale images up or down|

These techniques are fundamental for **image preprocessing** in computer vision — they are often used before tasks like feature extraction, segmentation, or model inference.
