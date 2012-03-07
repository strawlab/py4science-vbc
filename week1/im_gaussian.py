import cv
import sys

import getfile

lena = "lena-color.png"

img = cv.LoadImageM(getfile.get_from_strawlab("week1/" + lena))
cv.Smooth(img, img, smoothtype=cv.CV_GAUSSIAN, param1=11)
cv.SaveImage("smoothed-"+lena, img)

