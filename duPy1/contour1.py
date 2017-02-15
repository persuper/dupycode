import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass

#---------------------------------------------------------------------
#从摄像头中取得图像吧！公用
cap = cv2.VideoCapture(0)
#取得图像尺寸
wid = int(cap.get(3))
hei = int(cap.get(4))
        
#创建空白图像
img = np.zeros((wid,hei),np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('val','image',0,255,nothing)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        cv2.imshow('image',frame)
        
        th=cv2.getTrackbarPos('val','image')
        #frame = cv2.flip(frame,0)
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,th,255,0)

        image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        img2 = cv2.drawContours(frame, contours, -1, (0,255,0), 3)
        cv2.imshow('Camera imaging 2',img2)

        img = frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

#---------------------------------------------------------------------

#im = cv2.imread('test.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#绘制独立轮廓，如第四个轮廓：
#img2 = cv2.drawContour(img, contours, -1, (0,255,0), 3)
#但是大多数时候，下面的方法更有用：


cv2.imshow("con", imgray)

cv2.destroyAllWindows()
