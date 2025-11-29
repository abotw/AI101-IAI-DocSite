
```python
import numpy as np  
import dlib  
import cv2  
from sklearn.metrics.pairwise import euclidean_distances  
from PIL import Image, ImageDraw, ImageFont  
  
  
# ------------------------------------------------------------  
# Utility Functions  
# ------------------------------------------------------------  
  
def mouth_aspect_ratio(shape):  
    """  
    Compute MAR (Mouth Aspect Ratio).    Uses several vertical distances divided by the horizontal width.    """    A = euclidean_distances(shape[50].reshape(1, 2), shape[58].reshape(1, 2))  
    B = euclidean_distances(shape[51].reshape(1, 2), shape[57].reshape(1, 2))  
    C = euclidean_distances(shape[52].reshape(1, 2), shape[56].reshape(1, 2))  
    D = euclidean_distances(shape[48].reshape(1, 2), shape[54].reshape(1, 2))  
  
    return ((A + B + C) / 3) / D  
  
  
def mouth_jaw_ratio(shape):  
    """  
    Compute MJR (Mouth-Opening / Jaw Width Ratio).    Larger values indicate wider mouth opening.    """    M = euclidean_distances(shape[48].reshape(1, 2), shape[54].reshape(1, 2))  # Mouth width  
    J = euclidean_distances(shape[3].reshape(1, 2), shape[13].reshape(1, 2))   # Jaw width  
    return M / J  
  
  
def put_chinese_text(img, text, position, color=(0, 255, 0), size=50):  
    """  
    Draw Chinese text onto an OpenCV BGR image using PIL.    """    if isinstance(img, np.ndarray):  
        pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  
    else:  
        pil_img = img  
  
    draw = ImageDraw.Draw(pil_img)  
    font = ImageFont.truetype("fz-hei.ttf", size, encoding="utf-8")  
  
    draw.text(position, text, color, font=font)  
    return cv2.cvtColor(np.asarray(pil_img), cv2.COLOR_RGB2BGR)  
  
  
# ------------------------------------------------------------  
# Initialize Detector and Webcam  
# ------------------------------------------------------------  
  
detector = dlib.get_frontal_face_detector()  
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  
  
cap = cv2.VideoCapture(0)  
  
# ------------------------------------------------------------  
# Main Loop  
# ------------------------------------------------------------  
while True:  
    ret, frame = cap.read()  
    if not ret:  
        print("Failed to read frame.")  
        break  
  
    faces = detector(frame, 0)  
    for face in faces:  
        # Extract 68 facial landmarks  
        shape = predictor(frame, face)  
        shape = np.array([[p.x, p.y] for p in shape.parts()])  
  
        mar = mouth_aspect_ratio(shape)[0][0]  
        mjr = mouth_jaw_ratio(shape)[0][0]  
  
        result = "正常"  
  
        if mar > 0.5:  
            result = "大笑"  
        elif mjr > 0.45:  
            result = "微笑"  
  
        print(f"MAR={mar:.3f}, MJR={mjr:.3f}, Result={result}")  
  
        frame = put_chinese_text(frame, result, (50, 100))  
  
        mouth_hull = cv2.convexHull(shape[48:61])  
        cv2.drawContours(frame, [mouth_hull], -1, (0, 255, 0), 1)  
  
    cv2.imshow("Frame", frame)  
  
    if cv2.waitKey(1) == 27:  # ESC to exit  
        break  
  
cap.release()  
cv2.destroyAllWindows()
```