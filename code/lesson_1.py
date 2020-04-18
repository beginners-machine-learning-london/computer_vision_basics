# basic images operations

# 1. Accessing and Modifying pixel values
import cv2
import numpy as np

# loads an image
img = cv2.imread('messi5.jpg')

# access a pixel value by its row and column coordinates
# it returns an BlueGreenRed array
px = img[100,100]
print(px)
# [157 166 200]

# accessing only blue pixel
blue = img[100,100,0]
print(blue)
# 157

# modifying pixel values
img[100,100] = [255,255,255]
print(img[100,100])
# [255 255 255]


# 2. Accessing image properties
# It returns a tuple of number of rows, columns and channels (if image is color)
print(img.shape)
# (342, 548, 3)

# total number of pixels
print(img.size)
# image datatype 
print(img.dtype)

# Splitting and Merging Image Channels
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# adding images
x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x,y)) 
# 250+10 = 260 => 255
