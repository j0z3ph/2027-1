import cv2 as cv
import numpy as np

img = cv.imread("gominola.webp")
w, h, c = img.shape

img2 = 255 - img

cv.imshow("Gominola", img)
cv.imshow("Gominola 2", img2)
cv.waitKey()