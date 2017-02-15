import cv2
import numpy as np
import matplotlib.pyplot as plot
from matplotlib import pyplot as plt

img=cv2.imread("f:/aaa.bmp")
#cv2.imshow("sd",img)
#cv2.waitKey(0)

#cv2.namedWindow('ducap', cv2.WINDOW_NORMAL)

#创建摄像头对象
cap = cv2.VideoCapture(0)


#-----------------------------------------------------------------------
#逐帧显示实现视频播放
#在while循环中，利用摄像头对象的read()函数读取视频的某帧，并显示，然后等待1个单位时间，如果期间检测到了键盘输入q，则退出，即关闭窗口。
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("du_capture", frame)

    img=frame

    k = cv2.waitKey(1)
    if k == ord('s'): ## wait for 's' key to save and exit
        cv2.imwrite("e:\ducap.png", frame)
        
    if k == ord('q'):
        break

#-----------------------------------------------------------------------
#使用Matplotib 是python 的一个绘图库，里头有各种各样的绘图方法
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()

#释放摄像头对象和窗口
#调用release()释放摄像头，调用destroyAllWindows()关闭所有图像窗口。
cap.release()
cv2.destroyAllWindows() 
