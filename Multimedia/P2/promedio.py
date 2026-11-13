import cv2 as cv
import numpy as np

img = cv.imread("gominola.webp")
w, h, c = img.shape

m = np.array([1/3,1/3,1/3])

img2 = np.clip(img.dot(m),0,255).astype('uint8')

cv.imshow("Gominola", img)
cv.imshow("Gominola 2", img2)
cv.waitKey()