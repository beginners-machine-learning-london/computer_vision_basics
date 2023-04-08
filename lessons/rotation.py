import cv2

image = cv2.imread("../img/lego.jpg")

# grab the dimensions of the image and calculate the center of the image
(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)
# rotate our image by 45 degrees
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import imutils

# rotate 180 degrees (flipping it upside down)
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)
