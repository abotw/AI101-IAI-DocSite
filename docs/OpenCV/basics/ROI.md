---
title: ROI
tags:
  - ROI
---

# ROI (Region of Interest)

In image processing and computer vision, we often do **not** need to analyze the entire image — instead, we focus on a **specific part** that matters, such as a face, an object, or a block of text.  
This focused area is called the **ROI**, or **Region of Interest**.

---

## 🧠 What Is ROI?

**ROI** stands for **Region of Interest**.  
It refers to a specific area within an image or video that you want to analyze, detect, recognize, or process further.

An ROI can be:

- **Manually selected** by the user (e.g., via coordinate slicing), or
    
- **Automatically detected** by algorithms (e.g., face detection, object tracking, OCR, etc.).
    

---

## 🧩 Extracting ROI in OpenCV

In OpenCV, images are stored as **NumPy arrays**.  
That means we can easily use array slicing to extract any rectangular area as an ROI.

```python
import cv2  
  
# Read an image  
img = cv2.imread('ex.jpg')  
  
# Extract ROI (rows 30–230, columns 100–300)  
roi = img[30:230, 100:300]  
  
# Display the original image and ROI  
cv2.imshow('Original', img)  
cv2.imshow('ROI', roi)  
  
cv2.waitKey(0)  
cv2.destroyAllWindows()
```

---

## 🔍 Code Explanation

|Code|Description|
|---|---|
|`a = cv2.imread('timg98.jpg')`|Reads the image as a NumPy array.|
|`b = a[30:230, 100:300]`|Extracts a rectangular ROI using NumPy slicing.|
|`cv2.imshow('yuantu', a)`|Displays the original image.|
|`cv2.imshow('qiepian', b)`|Displays the extracted ROI.|
|`cv2.waitKey(0)`|Waits for a key press indefinitely.|
|`cv2.destroyAllWindows()`|Closes all image display windows.|

---

## 📐 Coordinate System

In OpenCV, image coordinates follow the same convention as NumPy arrays:

- **First index (rows)** → y-axis (vertical)
    
- **Second index (columns)** → x-axis (horizontal)
    

Thus:

```python
roi = img[y1:y2, x1:x2]
```

where:

- `(x1, y1)` is the **top-left** corner, and
    
- `(x2, y2)` is the **bottom-right** corner.
    

---

## ⚙️ Common Use Cases

ROIs are widely used in many computer vision tasks, such as:

- Focusing analysis on specific regions
    
- Extracting candidate areas in object detection
    
- Tracking moving objects in video streams
    
- Performing OCR (text recognition) within detected text regions
    
- Reducing computation time and memory usage
    

---

## 💡 Tips

- ROI slicing in OpenCV does **not** create a new image copy — it returns a **view** of the original array.  
    Any modification to the ROI will also affect the original image.
    
- To create an independent copy, use:
    
    ```python
    roi = a[30:230, 100:300].copy()
    ```
    

---

## 📚 Further Reading

- [OpenCV Docs — Basic Operations on Images](https://docs.opencv.org/)
    
- [NumPy Array Indexing](https://numpy.org/doc/stable/user/basics.indexing.html)
    
- [What Is ROI in Computer Vision (Medium)](https://medium.com/)
    

---

## ✅ Summary

The **Region of Interest (ROI)** is a fundamental concept in image analysis.  
By using NumPy slicing, you can quickly isolate and manipulate key regions in your images — a crucial step for object detection, recognition, and visual understanding in computer vision workflows.
