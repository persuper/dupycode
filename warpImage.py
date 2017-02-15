import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('e:/ducap.png',0)
rows,cols=img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(300,300))
plt.subplot(121,plt.imshow(img),plt.title('Input'))
plt.subplot(121,plt.imshow(img),plt.title('Output'))
plt.show()

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('e:\ducap.png',0)
rows,cols= img.shape

pts1=np.float32([[50,50],[200,50],[50,200]])
pts2=np.float32([[10,100],[200,50],[100,250]])

M=cv2.getAffineTransform(pts1,pts2)
dst=cv2.warpAffine(img,M,(cols,rows))
plt.subplot(121, plt.imshow(img), plt.title('Input'))
plt.subplot(121, plt.imshow(img), plt.title('Output'))
plt.show()

# 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
# 可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
M=cv2.getRotationMatrix2D((cols/2,rows/2),45,0.6)
# 第三个参数是输出图像的尺寸中心
dst=cv2.warpAffine(img,M,(2*cols,2*rows))
while(1):
         cv2.imshow('img',dst)
         if cv2.waitKey(1)&0xFF==27:
                  break
cv2.destroyAllWindows()
'''
