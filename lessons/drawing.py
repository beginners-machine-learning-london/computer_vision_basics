import numpy as np
import cv2

# Create a black canvas of size 500x500
canvas = np.zeros((500, 500, 3), dtype=np.uint8)

# Define the range of possible colors
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Draw 100 random shapes on the canvas
for i in range(100):
    # Choose a random color from the colors list
    color = colors[np.random.randint(0, len(colors))]

    # Choose a random shape to draw
    shape = np.random.randint(0, 3)

    # Define the shape parameters
    x1 = np.random.randint(0, 500)
    y1 = np.random.randint(0, 500)
    x2 = np.random.randint(0, 500)
    y2 = np.random.randint(0, 500)
    thickness = np.random.randint(1, 10)

    # Draw the shape on the canvas
    if shape == 0:
        # Draw a line
        cv2.line(canvas, (x1, y1), (x2, y2), color, thickness)
    elif shape == 1:
        # Draw a rectangle
        cv2.rectangle(canvas, (x1, y1), (x2, y2), color, thickness)
    elif shape == 2:
        # Draw a circle
        radius = np.random.randint(10, 100)
        cv2.circle(canvas, (x1, y1), radius, color, thickness)

# Show the resulting image
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
