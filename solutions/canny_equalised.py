import cv2
import numpy as np
import matplotlib.pyplot as plt

def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged


# load the image and convert it to grayscale
image = cv2.imread('../img/tree.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = auto_canny(gray)

eq = cv2.equalizeHist(gray)
eq_edges = auto_canny(eq)

plt.figure(figsize=(20, 10))
plt.subplot(221), plt.imshow(gray, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(eq, cmap='gray')
plt.title('Equalised Image'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(eq_edges, cmap='gray')
plt.title('Canny Edge Equalised Image'), plt.xticks([]), plt.yticks([])

plt.show()
