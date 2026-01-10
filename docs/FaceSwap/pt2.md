
# Part 2

## original code

```python
import cv2  
import numpy as np  
import dlib  
  
img = cv2.imread("face.jpg")  
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
mask = np.zeros_like(img_gray)  
  
detector = dlib.get_frontal_face_detector()  
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  
  
faces = detector(img_gray)  
for face in faces:  
    landmarks = predictor(img_gray, face)  
    landmarks_points = []  
  
    for i in range(68):  
        x, y = landmarks.part(i).x, landmarks.part(i).y  
        landmarks_points.append((x, y))  
  
        # cv2.circle(img, (x, y), 3, (0, 0, 255), -1)  
  
    points = np.array(landmarks_points)  
    convex_hull = cv2.convexHull(points)  
    # cv2.polylines(img, [convex_hull], True, (255, 0, 0), 2)  
  
    cv2.fillConvexPoly(mask, convex_hull, 255)  
  
    face_image_1 = cv2.bitwise_and(img, img, mask=mask)  
  
    # Delaunay triangulation  
    rect = cv2.boundingRect(convex_hull)  
    # (x, y, w, h) = rect  
    # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  
    subdiv = cv2.Subdiv2D(rect)  
    subdiv.insert(landmarks_points)  
    triangles = subdiv.getTriangleList()  
    triangles = np.array(triangles, dtype=np.int32)  
  
    for t in triangles:  
        pt1 = (t[0], t[1])  
        pt2 = (t[2], t[3])  
        pt3 = (t[4], t[5])  
  
        cv2.line(img, pt1, pt2, (0, 255, 0), 1)  
        cv2.line(img, pt2, pt3, (0, 255, 0), 1)  
        cv2.line(img, pt3, pt1, (0, 255, 0), 1)  
  
cv2.imshow("Image", img)  
# cv2.imshow("Face Image 1", face_image_1)  
# cv2.imshow("Mask", mask)  
cv2.waitKey(0)  
cv2.destroyAllWindows()
```
