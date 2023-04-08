import cv2
import numpy as np

# load the image and show it
image = cv2.imread("../img/lego.jpg")
(B, G ,R) = cv2.split(image)

# show each channel individually

zeros = np.zeros(image.shape[:2], dtype = "uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# merge the image back together again in an incorrect order
rgb_merged = cv2.merge([R, G, B])
rbg_merged = cv2.merge([R, B, G])
cv2.imshow("RGB Merged", rgb_merged)
cv2.imshow("RBG Merged", rbg_merged)
cv2.waitKey(0)
cv2.destroyAllWindows()