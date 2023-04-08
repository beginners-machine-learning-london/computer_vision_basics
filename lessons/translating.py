import cv2
import imutils
import numpy as np

# Load the input image
image = cv2.imread('../img/lego.jpg')

# Define the translation matrix
Tx, Ty = 50, 100
M = np.float32([[1, 0, Tx], [0, 1, Ty]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
# now, let's shift the image 50 pixels to the left and 90 pixels up, we
# accomplish this using negative values

Tx, Ty = -50, -100
M = np.float32([[1, 0, Tx], [0, 1, Ty]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

# Display the input and translated images side by side
cv2.imshow('Input Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import imutils

shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
