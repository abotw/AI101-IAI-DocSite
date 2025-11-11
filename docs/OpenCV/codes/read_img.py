# read and display an image
import cv2

# load a color image in grayscale
img = cv2.imread("avatar.jpg", cv2.IMREAD_UNCHANGED)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()