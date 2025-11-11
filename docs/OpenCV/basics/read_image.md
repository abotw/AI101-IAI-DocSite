---
title: Read an Image
category: opencv-basics
tags:
  - opencv
  - image
  - tutorial
---

# Read an Image

This example shows how to read and display an image using OpenCV.

## Code Example

```python
import cv2

# Read an image from file
img = cv2.imread('assets/images/cat.jpg')

# Display the image
cv2.imshow('Cat', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Notes

- `cv2.imread(path)` loads the image as a NumPy array.
- Use `cv2.IMREAD_GRAYSCALE` to load as grayscale.
- Remember to call `cv2.waitKey(0)`; otherwise, the window will close immediately.

