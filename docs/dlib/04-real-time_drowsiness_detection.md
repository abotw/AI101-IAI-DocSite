
# Real-time Drowsiness Detection

## v1

```python
import dlib  
import cv2  
import numpy as np  
  
# ---------- EAR computation ----------  
def compute_EAR(landmarks, eye_points):  
    # A = |p2 - p6|  
    A = np.linalg.norm( np.array([landmarks.part(eye_points[1]).x, landmarks.part(eye_points[1]).y]) -  
                        np.array([landmarks.part(eye_points[5]).x, landmarks.part(eye_points[5]).y]) )  
  
    # B = |p3 - p5|  
    B = np.linalg.norm( np.array([landmarks.part(eye_points[2]).x, landmarks.part(eye_points[2]).y]) -  
                        np.array([landmarks.part(eye_points[4]).x, landmarks.part(eye_points[4]).y]) )  
  
    # C = |p1 - p4|  
    C = np.linalg.norm( np.array([landmarks.part(eye_points[0]).x, landmarks.part(eye_points[0]).y]) -  
                        np.array([landmarks.part(eye_points[3]).x, landmarks.part(eye_points[3]).y]) )  
  
    EAR = ((A + B) / 2.0) / C  
    return EAR  
  
  
# ---------- dlib init ----------  
webcam = cv2.VideoCapture(0)  
detector = dlib.get_frontal_face_detector()  
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  
  
# left eye landmark index (dlib 68-model)  
LEFT_EYE = [36, 37, 38, 39, 40, 41]  
RIGHT_EYE = [42, 43, 44, 45, 46, 47]  
  
EAR_THRESHOLD = 0.3        # EAR below this → closed eyes  
CONSEC_FRAMES = 15         # how many frames of closure → fatigue alarm  
  
counter = 0                # closed-eye frame count  
  
while True:  
    ret, frame = webcam.read()  
    if not ret:  
        break  
  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    faces = detector(gray)  
  
    for face in faces:  
        landmarks = predictor(gray, face)  
  
        # Compute EAR for both eyes  
        leftEAR = compute_EAR(landmarks, LEFT_EYE)  
        rightEAR = compute_EAR(landmarks, RIGHT_EYE)  
        EAR = (leftEAR + rightEAR) / 2.0  
  
        # Draw EAR text  
        cv2.putText(frame, f"EAR: {EAR:.3f}", (30, 30),  
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)  
  
        # ---- Fatigue detection ----  
        if EAR < EAR_THRESHOLD:  
            counter += 1  
            cv2.putText(frame, "Eyes Closed", (30, 70),  
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)  
  
            # Alarm when too many consecutive closed-eye frames  
            if counter >= CONSEC_FRAMES:  
                cv2.putText(frame, "!!! FATIGUE WARNING !!!", (30, 120),  
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)  
        else:  
            counter = 0  
            cv2.putText(frame, "Eyes Open", (30, 70),  
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)  
  
        # Draw 68 landmarks  
        for n in range(68):  
            x = landmarks.part(n).x  
            y = landmarks.part(n).y  
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)  
            cv2.putText(frame, str(n), (x, y),  
                        cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1)  
  
    cv2.imshow("Fatigue Monitor", frame)  
  
    if cv2.waitKey(1) == 27:     # ESC  
        break  
  
webcam.release()  
cv2.destroyAllWindows()
```

## v2

```python
import numpy as np  
import dlib  
import cv2  
from sklearn.metrics.pairwise import euclidean_distances  
from PIL import Image, ImageDraw, ImageFont  
  
  
# -----------------------------------------------  
# Compute Eye Aspect Ratio (EAR)  
# -----------------------------------------------  
def compute_ear(eye_points):  
    """  
    Compute Eye Aspect Ratio (EAR) using 6 landmark points.    EAR = (||p2-p6|| + ||p3-p5||) / (2 * ||p1-p4||)  
    Args:        eye_points (list): Six (x, y) tuples from facial landmarks.  
    Returns:        float: EAR value.    """    eye = np.array(eye_points)  
  
    A = euclidean_distances([eye[1]], [eye[5]])[0][0]  
    B = euclidean_distances([eye[2]], [eye[4]])[0][0]  
    C = euclidean_distances([eye[0]], [eye[3]])[0][0]  
  
    ear = (A + B) / (2.0 * C)  
    return ear  
  
  
# -----------------------------------------------  
# Draw Chinese text on OpenCV image  
# -----------------------------------------------  
def draw_chinese_text(img, text, position, text_color=(0, 255, 0), text_size=30):  
    """  
    Draw Chinese text on a BGR OpenCV image using PIL.  
    Args:        img (ndarray): BGR image.        text (str): Text to draw.        position (tuple): (x, y) position.        text_color (tuple): BGR color.        text_size (int): Font size.  
    Returns:        ndarray: Updated BGR image.    """    # Convert to PIL image    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  
    drawer = ImageDraw.Draw(pil_img)  
  
    # Load font (ensure `simhei.ttf` exists)  
    font = ImageFont.truetype("fz-hei.ttf", text_size, encoding="utf-8")  
  
    # Draw text  
    drawer.text(position, text, fill=text_color, font=font)  
  
    # Convert back to OpenCV BGR  
    return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)  
  
  
# -----------------------------------------------  
# Draw the convex hull of the eye  
# -----------------------------------------------  
def draw_eye_hull(img, eye_points):  
    """  
    Draw convex hull of an eye region.  
    Args:        img (ndarray): BGR frame.        eye_points (list): Eye landmark (6 points).    """    hull = cv2.convexHull(np.array(eye_points))  
    cv2.drawContours(img, [hull], -1, (0, 255, 0), 1)  
  
  
# ==============================================================  
# Main - Real-time Drowsiness Detection  
# ==============================================================  
  
EAR_THRESHOLD = 0.30        # EAR below this → possibly closed eyes  
EAR_CONSEC_FRAMES = 50      # Number of consecutive frames before alert  
  
frame_counter = 0  
  
detector = dlib.get_frontal_face_detector()  
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  
  
cap = cv2.VideoCapture(0)  
  
while True:  
    ret, frame = cap.read()  
    if not ret:  
        print("Failed to capture frame.")  
        break  
  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    faces = detector(gray)  
  
    for face in faces:  
        shape = predictor(gray, face)  
        shape_np = np.array([[p.x, p.y] for p in shape.parts()])  
  
        left_eye = shape_np[36:42]  
        right_eye = shape_np[42:48]  
  
        left_ear = compute_ear(left_eye)  
        right_ear = compute_ear(right_eye)  
        ear = (left_ear + right_ear) / 2.0  
  
        # Eye drawing  
        draw_eye_hull(frame, left_eye)  
        draw_eye_hull(frame, right_eye)  
  
        # Fatigue detection  
        if ear < EAR_THRESHOLD:  
            frame_counter += 1  
  
            if frame_counter > EAR_CONSEC_FRAMES:  
                frame = draw_chinese_text(frame, "！！！危险！！！", (250, 250), (0, 0, 255), 40)  
        else:  
            frame_counter = 0  
  
        # EAR display  
        info_text = f"EAR: {ear:.2f}"  
        frame = draw_chinese_text(frame, info_text, (30, 30), (0, 255, 0), 28)  
  
    cv2.imshow("Drowsiness Detection", frame)  
  
    if cv2.waitKey(1) == 27:  # ESC key  
        break  
  
cap.release()  
cv2.destroyAllWindows()
```
