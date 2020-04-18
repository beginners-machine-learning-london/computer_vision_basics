import argparse
import cv2

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help = 'Path to the image')
ap.add_argument('-o', '--output', required=False, help = 'Path to saving the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

cv2.waitKey(0)

# crop the image by slicing the matrix
cropped = image[100: 1000, 10:300]
cv2.imshow('Edited', cropped)

cv2.waitKey(0)

# save the image to specified path
cv2.imwrite(f'{args["output"]}/cropped_coding.jpg', cropped)

