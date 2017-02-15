import cv2
import numpy as np
img = cv2.imread('e:\ducap.png',1)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#tabel

# 别忘了中括号[img],[0],None,[256],[0,256]，只有mask 没有中括号
hist = cv2.calcHist([img2],[0],None,[256],[0,256])

cv2.imshow("his", hist)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
#cv2.THRESH_BINARY_INV+
#contours = cv2.findContours(thresh,2,1)
cv2.imshow("thr", thresh)

image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("image", image)

cnt = contours[0]
hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)




#ret,thresh = cv2.threshold(image,127,255,0)
#cv2.imshow("df", thresh)
contours = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cnt = contours[0]
#M = cv2.moments(cnt)
#area = cv2.contourArea(cnt)

img3=np.zeros(img.shape, np.uint8)
img3=img
cv2.drawContours(image, contours, -1, (0,0,255), -1)
cv2.imshow("con", img3)

