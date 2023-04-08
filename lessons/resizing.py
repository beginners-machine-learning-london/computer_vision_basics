import cv2
import imutils

image = cv2.imread("../img/snowy_i.png")

resized = imutils.resize(image, width=100)
cv2.imshow("Original", image)

# construct the list of interpolation methods
methods = [
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
    ("cv2.INTER_AREA", cv2.INTER_AREA),
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
    ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
# loop over the interpolation methods
for (name, method) in methods:
    # increase the size of the image by 3x using the current interpolation
    # method
    resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
    cv2.imshow("Method: {}".format(name), resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
