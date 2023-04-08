import cv2
import numpy as np

# Create a black canvas
img = np.zeros((500, 800, 3), dtype=np.uint8)

# Draw text on the canvas
text = "Hello, AI Builders in OpenCV!"
org = (50, 250)
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1.5
color = (0, 255, 0)
thickness = 2
lineType = cv2.LINE_AA
cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)

# Display the image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
