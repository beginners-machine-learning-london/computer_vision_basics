import cv2

# Load the image
img = cv2.imread("../img/coding.png")

# Convert the image from BGR to LAB color space
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Split the LAB channels
l, a, b = cv2.split(lab)

# Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to the L channel
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
l_clahe = clahe.apply(l)

# Merge the LAB channels back together
lab_clahe = cv2.merge((l_clahe, a, b))

# Convert the LAB image back to BGR color space
result = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2BGR)

# Display the result
cv2.imshow("Original Image", img)
cv2.imshow("Colour Corrected Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
