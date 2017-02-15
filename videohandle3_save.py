# -*- coding: utf-8 -*-
"""
Created on Fri Jan 3 21:06:22 2014

@author: duan
"""
import numpy as np
import cv2

#定义鼠标事件函数
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(imgOut,(x,y),100,(255,0,0),1)#-1)



# 新图象
imgOut=np.zeros((512,512,3), np.uint8)
# 创建图像与窗口并将窗口与回调函数绑定
cv2.namedWindow('imgOut')
cv2.setMouseCallback('imgOut',draw_circle)
while(1):
    cv2.imshow('imgOut',imgOut)
    if cv2.waitKey(20)&0xFF==27:
        break
    


cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('e:\output22.avi',fourcc, 20.0, (640,480))



while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        #frame = cv2.flip(frame,0)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        #ret, mask = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
        ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        # noise removal
        kernel = np.ones((3,3), np.uint8 )
        opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN, kernel, iterations = 2)

        # sure background area
        sure_bg = cv2.dilate(opening,kernel,iterations=3)

        # Finding sure foreground area
        dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
        ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

        # Finding unknown region
        sure_fg = np.uint8(sure_fg)
        unknown = cv2.subtract(sure_bg,sure_fg)
        
 
        # write the frame
        out.write(frame)


        cv2.imshow('src',frame)
        #cv2.imshow('frame',opening)

        #取得图像尺寸
        wid = int(cap.get(3))
        hei = int(cap.get(4))


        # Create a black image
        # img2=np.zeros((512,512,3), np.uint8)
        # Draw a diagonal blue line with thickness of 5 px
        cv2.line(opening,(0,0),(wid-1,hei-1),(255,0,0),5)
        cv2.rectangle(opening,(5,5),(wid-5, hei-5),(255,255,0),3)
        cv2.circle(opening, ( int(wid/2), int(hei/2)), 40, (255,0,255), 1)#-1)
        cv2.ellipse(opening,(int(wid/2), int(hei/2)),(100,50),0,0,180,255, 1) #-1)

        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(opening,'Dujianjun',(int(wid/2)-60,50), font, 1,(255,255,255),1)
        
        cv2.imshow('img2',opening)

        imgOut = opening
                
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

#cv2.destroyAllWindows()


# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
