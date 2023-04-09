import cv2
import numpy as np

# Read the input image
img = cv2.imread('../img/beach.png')

# Convert the image from RGB to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the color range to be extracted (blue color in this case)
lower_range = np.array([100,50,50])
upper_range = np.array([130,255,255])

# Create a mask for the blue color range
mask = cv2.inRange(hsv, lower_range, upper_range)

# Apply the mask to the original image
output = cv2.bitwise_and(img, img, mask=mask)

# Display the input and output images side by side
cv2.imshow('Input Image', img)
cv2.imshow('Output Image', output)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
