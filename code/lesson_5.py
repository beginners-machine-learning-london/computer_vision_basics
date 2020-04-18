# Lesson 5 - Identifying Contours of objects in Images

import numpy as np
import cv2

img_file = '../img/coding.jpg'

# finding contour
img = cv2.imread(img_file)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
# v2.CHAIN_APPROX_SIMPLE returns only the 4 extremity points of an image
# use cv2.CHAIN_APPROX_NONE if you want all the points of the contour

# draw all the contours
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

# draw an individual contour
cnt = contours[4]
img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

# image moments
img = cv2.imread(img_file,0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
print(M)

# centroid (x,y)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

# contour area
area = cv2.contourArea(cnt)

# contour perimeter
perimeter = cv2.arcLength(cnt,True)

# aspect ratio (ratio of width to height of bounding rect of the object)
x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h

# extent (ratio of contour area to bounding rectangle area)
rect_area = w*h
extent = float(area)/rect_area

# solidity (ratio of contour area to its convex hull area)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area





