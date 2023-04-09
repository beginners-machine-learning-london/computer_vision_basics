import cv2
import numpy as np

image = cv2.imread("../img/lego.jpg")
cv2.imshow("Original", image)

# Masking allows us to focus only on parts of an image that interest us.
# A mask is the same size as our image, but has only two pixel values,
# 0 and 255. Pixels with a value of 0 are ignored in the orignal image,
# and mask pixels with a value of 255 are allowed to be kept. For example,
# let's construct a rectangular mask that displays only the person in
# the image

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)
cv2.imshow("Mask", mask)

# Apply our mask -- notice how only the person in the image is cropped out
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np

image = cv2.imread("../img/lego.jpg")
cv2.imshow("Original", image)

# Create a black mask of the same size as the image
mask = np.zeros(image.shape[:2], dtype="uint8")

# Draw a star shape on the mask
center_coordinates = (mask.shape[1] // 2, mask.shape[0] // 2)
radius = mask.shape[0] // 2
num_vertices = 5
angle = 0
vertices = []
for i in range(num_vertices * 2):
    radius_multiplier = 1 if i % 2 == 0 else 0.5
    x = int(center_coordinates[0] + (radius * radius_multiplier * np.cos(angle)))
    y = int(center_coordinates[1] + (radius * radius_multiplier * np.sin(angle)))
    vertices.append((x, y))
    angle += np.pi / num_vertices
pts = np.array(vertices, np.int32)
cv2.fillPoly(mask, [pts], color=(255, 255, 255))
masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Mask", mask)
cv2.imshow("Complex Mask Applied to Image", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np

# Load the input image
img = cv2.imread('../img/lego.jpg')

# Create a binary mask for the star shape
mask = np.zeros(img.shape[:2], dtype=np.uint8)
center_coordinates = (mask.shape[1]//2, mask.shape[0]//2)
radius = mask.shape[0]//4
pts = np.array([[(center_coordinates[0], center_coordinates[1] - radius),
                 (center_coordinates[0] + radius//3, center_coordinates[1] - radius//3),
                 (center_coordinates[0] + radius, center_coordinates[1] - radius),
                 (center_coordinates[0] + radius//3, center_coordinates[1]),
                 (center_coordinates[0] + radius, center_coordinates[1] + radius),
                 (center_coordinates[0], center_coordinates[1] + radius//3),
                 (center_coordinates[0] - radius, center_coordinates[1] + radius),
                 (center_coordinates[0] - radius//3, center_coordinates[1]),
                 (center_coordinates[0] - radius, center_coordinates[1] - radius),
                 (center_coordinates[0] - radius//3, center_coordinates[1] - radius//3)]],
               dtype=np.int32)
cv2.fillPoly(mask, pts, color=255)

# Apply the mask to the input image using bitwise_xor
masked_img = cv2.bitwise_xor(img, img, mask=mask)

# Display the results
cv2.imshow('Input Image', img)
cv2.imshow('Mask', mask)
cv2.imshow('Masked Image', masked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
