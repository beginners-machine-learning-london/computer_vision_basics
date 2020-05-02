import cv2
import numpy as np

image = cv2.imread('../img/seal.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# compute gradients along the X and Y axis, respectively
gX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
gY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

# compute the gradient magnitude and orientation respectively
mag = np.sqrt((gX ** 2) + (gY ** 2))
orientation = np.arctan2(gY, gX) * (180 / np.pi) % 180

print(f'Gradient at pixel (80, 80) has magnitude {mag[80, 80]} and orientation {orientation[80, 80]} degrees')
