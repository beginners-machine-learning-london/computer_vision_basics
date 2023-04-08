import cv2
import numpy as np
import random

# Define the input text
text = "openCV is a great library for image processing and computer vision"

# Create an empty black canvas with size 500x500
canvas = np.zeros((500, 500, 3), dtype=np.uint8)

# Split the text into words
words = text.split()

# Set the font parameters
font_face = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 2

# Randomly choose a color for each word
colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in words]

# Define the initial position for the first word
pos_x, pos_y = 50, 50

# Loop over each word and draw it on the canvas
for i, word in enumerate(words):
    # Get the size of the word
    (w, h), _ = cv2.getTextSize(word, font_face, font_scale, thickness)

    # Calculate the position of the word
    if pos_x + w > canvas.shape[1] - 50:
        pos_x = 50
        pos_y += h + 10

    # Draw the word on the canvas
    cv2.putText(canvas, word, (pos_x, pos_y), font_face, font_scale, colors[i], thickness)

    # Update the position for the next word
    pos_x += w + 10

# Show the final image
cv2.imshow("Word Cloud", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
