# Lesson 6 - Histograms and Image Enhancements by Equalising

import numpy as np
import cv2


img = cv2.imread('../img/coding.jpg',0)

# find histogram in opencv
hist = cv2.calcHist([img],[0],None,[256],[0,256])

# find histogram in numpy
hist,bins = np.histogram(img.ravel(),256,[0,256])

# plotting histograms - matplotlib
from matplotlib import pyplot as plt

plt.hist(img.ravel(),256,[0,256])
plt.show()

# with BGR results
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

plt.show()

# equalization 
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res.png',res)

# 2d histogram
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256]) 
#First argument is H plane, second one is the S plane, third is number of bins for each and fourth is their range
cv2.imshow()

# backprojection
img = cv2.imread('../img/coding.png')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# TODO: update target img file
target = cv2.imread('rose.png')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

# calculating object histogram
roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )

# normalize histogram and apply backprojection
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(dst,-1,disc,dst)

# threshold and binary AND
ret,thresh = cv2.threshold(dst,50,255,0)
thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(target,thresh)

res = np.vstack((target,thresh,res))
cv2.imwrite('res.jpg',res)
