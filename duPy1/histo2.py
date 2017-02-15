import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('e:/ducap.png',0)
ret, mask = cv2.threshold(img, 127, 255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
masked_img = cv2.bitwise_and(img,img,mask = mask)


# hiastogram equation is ok for the gray and rgb images.
# Equalization!
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))
cv2.imshow("res", res)


#flatten() 将数组变成一维
hist,bins = np.histogram(masked_img.flatten(),256,[0,256])
# 计算累积分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(masked_img.flatten(),256,[1,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

cv2.imshow("img", masked_img)
