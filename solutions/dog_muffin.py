import cv2
import numpy as np

def show_image(image, cmap = None, fig_size = (10, 10)):
    fig, ax = plt.subplots(figsize=fig_size)
    ax.imshow(image, cmap = cmap)
    ax.axis('off')
    plt.show()

image = np.flip(cv2.imread('../img/dog_muffin.jpg'), axis=2)
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (90, 120), (160, 190), 255, -1)

masked = cv2.bitwise_and(image, image, mask=mask)
show_image(masked)