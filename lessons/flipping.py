import cv2

image = cv2.imread("../img/lego.jpg")

cv2.imshow("Original", image)

# flip the image horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# flip the image vertically
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# flip the image along both axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

# Load the image
image = cv2.imread('../img/lego.jpg')
cv2.imshow('Original Image', image)

# Flip the image horizontally using NumPy
flipped_image = np.flip(image, axis=1)
cv2.imshow('Horizontally Flipped Image - Numpy', flipped_image)

# Flip the image vertically using NumPy
flipped_image = np.flip(image, axis=0)
cv2.imshow('Vertically Flipped Image - Numpy', flipped_image)

# Flip the image along both axes using NumPy
flipped_image = np.flip(image, axis=0)
flipped_image = np.flip(flipped_image, axis=1)
cv2.imshow('Flipped Image on both axes - Numpy', flipped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
