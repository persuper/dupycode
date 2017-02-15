import numpy as np
from matplotlib import pyplot as plt
import cv2
img = cv2.imread('e:/ducap.png',0)
# create a CLAHE object (Arguments are optional).
# 不知道为什么我没好到createCLAHE 这个模块
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
#cv2.imwrite('clahe_2.jpg',cl1)
cv2.imshow("cl1j", cl1)

#二维直方图

img2 = cv2.imread('e:/ducap.png',1)
hsv = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
plt.imshow(hist,interpolation = 'nearest')
plt.show()
