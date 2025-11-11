---
title: OpenCV Common Usages
category: Computer Vision
tags: [opencv, python, image-processing, ai]
---

# OpenCV Common Usages

## Introduction

**OpenCV (Open Source Computer Vision Library)** is an open-source computer vision and image-processing library originally developed by Intel. It provides a comprehensive set of tools for real-time image processing, computer vision, and machine learning tasks.  

OpenCV supports multiple languages — including **Python, C++, and Java** — and runs on various platforms such as Windows, macOS, Linux, and even mobile devices.

This document introduces OpenCV’s **most commonly used functions and workflows** to help you quickly get started with practical image and video processing tasks.

---

## 1. Installation and Import *

To install OpenCV for Python:

```bash
pip install opencv-python
pip install opencv-contrib-python
```

Import the library in your Python code:

```python
import cv2
```

---

## 2. Reading and Displaying Images *

OpenCV uses the `cv2.imread()` and `cv2.imshow()` functions to read and display images.

```python
import cv2

# Read an image
img = cv2.imread('example.jpg')

# Display the image in a window
cv2.imshow('Display Window', img)

# Wait for a key press
cv2.waitKey(0)
cv2.destroyAllWindows()
```

> 💡 `cv2.waitKey(0)` means the program will wait indefinitely for **a key press** before closing the window.

---

## 3. Image Properties and Basic Info *

You can easily access image dimensions, type, and pixel values.

```python
print(img.shape)   # (height, width, channels)
print(img.size)    # Total number of pixels
print(img.dtype)   # Data type, e.g., uint8
```

To access individual pixel values:

```python
px = img[100, 50]  # Get BGR value at (x=50, y=100)
print(px)
```

To modify pixels:

```python
img[100, 50] = [255, 255, 255]  # Set to white
```

---

## 4. Image Color Conversions

Color space conversion is fundamental in image processing.

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```

Common conversions:

- `cv2.COLOR_BGR2GRAY` — Convert to grayscale = 0
    
- `cv2.COLOR_BGR2RGB` — Convert from BGR to RGB
    
- `cv2.COLOR_BGR2HSV` — Convert to HSV color space
    

---

## 5. Image Resizing and Cropping

### Resizing:

```python
resized = cv2.resize(img, (400, 300))
```

### Cropping (via NumPy slicing):

```python
cropped = img[50:200, 100:400]
```

---

## 6. Drawing Shapes and Text

OpenCV allows drawing geometric shapes and adding text to images.

```python
cv2.line(img, (0, 0), (200, 200), (255, 0, 0), 3)
cv2.rectangle(img, (50, 50), (250, 150), (0, 255, 0), 2)
cv2.circle(img, (150, 100), 50, (0, 0, 255), -1)
cv2.putText(img, 'OpenCV', (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
```

---

## 7. Image Thresholding

Thresholding separates objects from the background by converting grayscale images into binary images.

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
```

Common types:

- `THRESH_BINARY`
    
- `THRESH_BINARY_INV`
    
- `THRESH_TRUNC`
    
- `THRESH_TOZERO`
    

---

## 8. Edge Detection

### Using Canny Edge Detector:

```python
edges = cv2.Canny(img, 100, 200)
```

This detects edges based on gradient changes and thresholds.

---

## 9. Image Blurring and Filtering

Blurring helps remove noise and smooth images.

```python
blur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
```

---

## 10. Contour Detection

Contours are useful for shape analysis and object detection.

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
```

---

## 11. Reading and Writing Video

### Reading from a file or camera:

```python
cap = cv2.VideoCapture('video.mp4')  # or 0 for webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Writing a video:

```python
out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (640, 480))
```

---

## 12. Face Detection (Using Haar Cascades)

OpenCV includes pretrained classifiers for face detection.

```python
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
```

---

## 13. Saving Images

```python
cv2.imwrite('output.jpg', img)
```

---

## 14. Common Tips

- OpenCV uses **BGR** color order, not RGB. Always convert if mixing with libraries like `matplotlib`.
    
- Use **NumPy operations** directly on images for speed.
    
- Always call `cv2.destroyAllWindows()` after displaying windows to release memory.
    

---

## 15. Summary

OpenCV provides a powerful, flexible, and efficient toolkit for:

- Image reading, manipulation, and filtering
    
- Object detection and tracking
    
- Video processing
    
- Real-time vision and machine learning
    

Mastering the common APIs listed here gives you a strong foundation for more advanced topics like **deep learning-based computer vision**, **AR**, or **autonomous systems**.

---

## References

- [OpenCV Official Documentation](https://docs.opencv.org/)
    
- [OpenCV GitHub Repository](https://github.com/opencv/opencv)
    
- [OpenCV Python Tutorials](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
    