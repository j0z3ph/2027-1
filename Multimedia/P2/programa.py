import cv2 as cv
import numpy as np

img = cv.imread("gominola.webp")
w, h, c = img.shape
#img2 = np.zeros((w,h,c), np.uint8)
img2 = np.clip(img + np.array([50]),0,255).astype('uint8')

#img2 = np.clip((img.astype("uint8") + img2.astype('uint8')).astype("uint8"),0,255)

#img2 = np.clip(img + 50,0,255)
 
# for x in range(0, h):
#     for y in range(0, w):
#         img2[x,y] = np.clip((img[x,y] - np.array([50,50,50])),0,255)

cv.imshow("Gominola", img)
cv.imshow("Gominola 2", img2)
cv.waitKey()