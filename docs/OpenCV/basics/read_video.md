---
title: Read and Display a Video File
category: opencv-basics
tags:
  - opencv
  - video
  - tutorial
---

# Read and Display a Video File

This example demonstrates how to **read and display a video file** frame by frame using OpenCV.  
It can also be adapted to display a live webcam feed by changing the video source.

---

## Code Example

```python
"""
-------------------------------------------------------
Video File Reading and Display using OpenCV
-------------------------------------------------------
"""

import cv2

# Open the video file (replace with 0 for webcam)
video_capture = cv2.VideoCapture('video.mp4')

# Check if the video file was opened successfully
if not video_capture.isOpened():
    print("Error: Cannot open the video file.")
    exit()

# Continuously read frames from the video
while True:
    ret, frame = video_capture.read()
    
    # If reading fails (end of video), break the loop
    if not ret:
        print("End of video or failed to read frame.")
        break

    # Convert the frame from BGR to grayscale (optional)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the current frame
    cv2.imshow('Video', frame_gray)
    
    # Wait for 60 ms and check if the 'Esc' key (27) is pressed
    if cv2.waitKey(60) == 27:
        print("Video playback interrupted by user.")
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()
```

---

## Explanation

- `cv2.VideoCapture('video.mp4')` creates a video capture object to read the file.  
    Use `cv2.VideoCapture(0)` to open the default webcam.
- `isOpened()` checks whether the file or device was successfully opened.
- The `while` loop continuously reads frames using `.read()`.
    - `ret` indicates whether the frame was successfully read.
    - `frame` is the actual image array.
- `cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)` converts the frame to grayscale.  
    This step is optional but often useful for processing.
- `cv2.imshow()` displays the frame in a window.
- `cv2.waitKey(60)` waits for 60 ms between frames;  
    pressing **Esc** (`key code 27`) stops playback.
- `release()` and `destroyAllWindows()` properly close resources.

---

## Notes

- Make sure the video file (`video.mp4`) is in the same directory as your script,  
    or provide an absolute path.
- To adjust playback speed, change the `cv2.waitKey()` delay (smaller = faster).
- If you only see a blank window, check whether the path to the video is correct.
- You can extend this script to record or process frames in real time.
