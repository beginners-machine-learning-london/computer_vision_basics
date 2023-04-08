import cv2
import imutils

# Load the two input images
img2 = cv2.imread('../img/beach.png')
img1 = cv2.imread('../img/lego.jpg')

cv2.imshow('First Image', img1)
cv2.imshow('Second Image', img2)


# Get the dimensions of the images
h1, w1 = img1.shape[:2]

# Resize the second image to match the size of the first image
img2 = imutils.resize(img2, width=w1)
h2r = img2.shape[0]

if h1 > h2r:
    img1 = img1[:h2r, :w1, :]
else:
    img2 = img2[:h1, :w1, :]


# Blend the images with alpha blending
alpha = 0.5
blended = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)

# Display the blended image
cv2.imshow('Blended Image', blended)
cv2.waitKey(0)
cv2.destroyAllWindows()
