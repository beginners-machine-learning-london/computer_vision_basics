# Lesson 2 & 3- Basic Image Processing Techniques (Cropping, Masking, 
# Geometric Transformations, Morphological Transformations)
# Kernels, Smoothing and Blurring Images

import cv2
import numpy as np

img_file = '../img/coding.jpg'
# scaling (resizing of the image)
img = cv2.imread(img_file)

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

# rotation
img = cv2.imread(img_file,0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))


# smoothing images
# 2D convolution (image filtering)
from matplotlib import pyplot as plt

img = cv2.imread(img_file)

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

# image blurring
blur = cv2.blur(img,(5,5))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

# gaussian blurring (filtering)
blur = cv2.GaussianBlur(img,(5,5),0)

# morphological transformations
# erosion (erodes away the boundaries of foreground object)
img = cv2.imread(img_file,0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

# dilation (oposite of ersosion. it increases the white region in the 
# image or size of foreground object increases)
dilation = cv2.dilate(img,kernel,iterations = 1)

# opening (erosion followed by dilation)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# closing (dilation followed by erosion)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
