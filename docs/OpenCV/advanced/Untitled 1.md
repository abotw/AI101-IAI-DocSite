
```python
import cv2  
  
# Create a CSRT tracker  
tracker = cv2.TrackerCSRT_create()  
  
# Tracking status flag  
tracking = False  
  
# Open webcam (0 = default camera)  
cap = cv2.VideoCapture(0)  
  
while True:  
    # Read a video frame  
    ret, frame = cap.read()  
    if not ret:  
        print("Error: Cannot read frame from camera.")  
        break  
  
    # Press 's' to select an ROI and start tracking  
    if cv2.waitKey(1) == ord('s'):  
        tracking = True  
  
        # Select the ROI on the current frame  
        roi = cv2.selectROI(  
            windowName='Tracking',  
            img=frame,  
            showCrosshair=False  
        )  
  
        # Initialize the tracker with the selected ROI  
        tracker.init(frame, roi)  
  
    # If tracking is active, update the tracker on the new frame  
    if tracking:  
        success, box = tracker.update(frame)  
  
        # If tracking succeeded, draw the bounding box  
        if success:  
            x, y, w, h = [int(v) for v in box]   # Ensure all values are ints  
            cv2.rectangle(  
                frame,  
                pt1=(x, y),  
                pt2=(x + w, y + h),  
                color=(0, 255, 0),  
                thickness=2  
            )  
        else:  
            cv2.putText(  
                frame,  
                "Tracking failed!",  
                (20, 40),  
                cv2.FONT_HERSHEY_SIMPLEX,  
                1.0,  
                (0, 0, 255),  
                2  
            )  
  
    # Display the result frame  
    cv2.imshow('Tracking', frame)  
  
    # Press ESC (key code 27) to exit  
    if cv2.waitKey(1) == 27:  
        break  
  
# Release camera and close windows  
cap.release()  
cv2.destroyAllWindows()
```