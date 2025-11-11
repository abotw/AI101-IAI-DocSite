
# Video File Reading and Display

```py
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