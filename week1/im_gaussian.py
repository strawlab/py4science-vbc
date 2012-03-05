#!/usr/bin/python
#
# gaussian-blur an image 
#
# usage: python im_gaussian.py filename
#

import cv
import sys

img = cv.LoadImageM(sys.argv[1])
cv.Smooth(img, img, smoothtype=cv.CV_GAUSSIAN, param1=11)
cv.SaveImage("smoothed_"+sys.argv[1], img)

