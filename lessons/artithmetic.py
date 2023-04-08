import cv2
import numpy as np

# Load image
img = cv2.imread('../img/lego.jpg')

# Adjust brightness by adding 50 to all pixels
brightened_img = cv2.add(img, 50)

# Display the original and the brightened image side by side
cv2.imshow('Original Image', img)
cv2.imshow('Brightened Image', brightened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# Load the image
img = cv2.imread('../img/lego.jpg')
# Adjust contrast by multiplying all pixels by 1.2
cv2_contrast = cv2.multiply(brightened_img, (1,1,1, 1), scale=1.2)
# Adjust contrast b
# y multitplying a scalar to the matrix image
np_contrast = img * 1.2
np_contrast = np_contrast.astype("uint8")
# Display the original and the contrast adjusted image side by side
cv2.imshow('Original Image', img)
cv2.imshow('CV2 - Contrast Adjusted Image', cv2_contrast)
cv2.imshow('Numpy - Contrast Adjusted Image', np_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()
