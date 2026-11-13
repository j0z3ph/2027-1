import cv2 as cv
import numpy as np

img = cv.imread("gominola.webp")
w, h, c = img.shape

img2 = cv.blur(img, (55,55))

# kernel
kernel = np.array([[0,-1,0],
                   [-1,5,-1],
                   [0,-1,0]])
img3 = cv.filter2D(img, -1, kernel)

cv.imshow("Gominola", img)
cv.imshow("Gominola 2", img2)
cv.imshow("Gominola 3", img3)
cv.waitKey()