# 🐍 Common OpenCV Usage Examples in Python

OpenCV is typically used in Python via the `cv2` module. Here are some of the most common, fundamental operations you'll encounter.

## 1. Reading, Displaying, and Writing Images

This is the most basic workflow for any image processing task.

- im: **im**age

|**Function**|**Purpose**|**Example Usage**|
|---|---|---|
|`cv2.imread()`|**Loads an image** from a file.|`img = cv2.imread('image.jpg')`|
|`cv2.imshow()`|**Displays the image** in a window.|`cv2.imshow('My Image', img)`|
|`cv2.waitKey()`|Waits for a **key press**. Essential for the display window to stay open.|`cv2.waitKey(0)`|
|`cv2.imwrite()`|**Saves the processed image** to a file.|`cv2.imwrite('new_image.png', img)`|
|`cv2.destroyAllWindows()`|Closes all open windows.|`cv2.destroyAllWindows()`|

## 2. Color Space Conversion

A frequent task is converting a standard color image (BGR in OpenCV, not RGB!) to **Grayscale** for simpler processing, or converting to the **HSV** (Hue, Saturation, Value) color space for easier color-based segmentation.

- **Grayscale Conversion:** Reduces the image from three channels (Blue, Green, Red) to one intensity channel.
    
```python
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
    
- **HSV Conversion:** Useful for isolating colors because the Hue channel is separated from brightness/intensity (Value).
    
```python
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```
    

## 3. Resizing and Scaling Images

To standardize input sizes for algorithms or to speed up processing, **resizing** is crucial.

- **By Fixed Size:** Resize to a specific width and height.
    
```Python
resized = cv2.resize(img, (200, 300)) # (width, height)
```
    
- **By Scale Factor:** Scale the image by a factor (e.g., half its size).
    
    
    
```Python
scaled = cv2.resize(img, None, fx=0.5, fy=0.5)
```
    

## 4. Simple Filtering/Blurring (Smoothing)

Filters are used to remove noise or smooth an image. The **Gaussian Blur** is one of the most common smoothing filters.

- The second argument `(5, 5)` is the **kernel size** (must be odd and positive). A larger kernel results in a greater blur.
    
```Python
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
```
    

## 5. Drawing Shapes and Text

OpenCV lets you draw geometric shapes or text directly onto an image, often used to **visualize detection results**.

|**Function**|**Purpose**|
|---|---|
|`cv2.rectangle()`|Draws a rectangle (often used for **Bounding Boxes**).|
|`cv2.circle()`|Draws a circle (useful for **keypoints**).|
|`cv2.line()`|Draws a line segment.|
|`cv2.putText()`|Draws text on the image.|

**Example (Drawing a Red Rectangle):**

```Python
# img, start_point, end_point, color (BGR), thickness
cv2.rectangle(img, (100, 100), (300, 300), (0, 0, 255), 2)
```

## 6. Edge Detection

**Canny Edge Detection** is a popular multi-stage algorithm used to find a wide range of edges in images, making them suitable for subsequent processing.

```Python
# The last two arguments are the minimum and maximum threshold values
edges = cv2.Canny(gray_img, 100, 200)
```

---

## 7. Video Processing and Webcam Access

OpenCV treats a video as a sequence of individual images (**frames**).

- **Reading Video/Webcam:** Use `cv2.VideoCapture()`. Pass the video file path or `0` for the default webcam.
    
    
    
```Python
cap = cv2.VideoCapture(0) # 0 for webcam

while True:
	ret, frame = cap.read() # Read a frame
	if not ret:
		break

	cv2.imshow('Video Feed', frame)

	# Exit loop on 'q' key press
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
```
