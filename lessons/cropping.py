import cv2

image = cv2.imread("../img/lego.jpg")

# cropping an image is accomplished using simple NumPy array slice
cropped_roi = image[100:300, 100:280, :]

cv2.imshow("ROI", cropped_roi)
cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
