import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load two images
img1 = cv2.imread('../img/beach.png')
img2 = cv2.imread('../img/lego.jpg')

# Convert images to HSV color space
hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

# Calculate histograms
hist1 = cv2.calcHist([hsv1], [0, 1], None, [180, 256], [0, 180, 0, 256])
hist2 = cv2.calcHist([hsv2], [0, 1], None, [180, 256], [0, 180, 0, 256])

# Normalize histograms
hist1 = cv2.normalize(hist1, hist1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
hist2 = cv2.normalize(hist2, hist2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

# Calculate chi-squared distance
distance = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)

print('Chi-squared distance:', distance) # prints