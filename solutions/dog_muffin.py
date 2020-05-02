import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.flip(cv2.imread('../img/dog_muffin.jpg'), axis=2)
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (90, 120), (160, 190), 255, -1)

masked = cv2.bitwise_and(image, image, mask=mask)
plt.figure(figsize=(20, 10))
plt.imshow(np.flip(masked, axis =2))
plt.title('Masked Image'), plt.xticks([]), plt.yticks([])
