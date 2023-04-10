import cv2

# Load the image
image = cv2.imread('../img/beach.png')

# Normalise the image
normalised = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Display the normalized image
cv2.imshow('Original Image', image)
print('Original Image', image)
cv2.imshow('Normalized Image', normalised)
print('Normalized Image', normalised)
cv2.waitKey(0)
cv2.destroyAllWindows()
