import cv2
import numpy as np
from matplotlib import pyplot as plt

#---------------------------------------------------------------------
#从摄像头中取得图像吧！公用
cap = cv2.VideoCapture(0)
#取得图像尺寸
wid = int(cap.get(3))
hei = int(cap.get(4))
        
#创建空白图像
img = np.zeros((wid,hei),np.uint8)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        #frame = cv2.flip(frame,0)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cv2.imshow('Camera imaging',frame)

        img = gray
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

#---------------------------------------------------------------------

#img=cv2.imread('e:/ducap.png',0)
ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
         plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
         plt.title(titles[i])
         plt.xticks([]),plt.yticks([])
plt.show()



#img = cv2.imread('e:/ducap.png',0)
# 中值滤波
img = cv2.medianBlur(img,5)
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#11 为Block size, 2 为C 值
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv2.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
         plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
         plt.title(titles[i])
         plt.xticks([]),plt.yticks([])
plt.show()
