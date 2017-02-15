import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('e:\ducap.png',0)
#plt.hist(img.ravel(),16,[0,255]);
#plt.show()
ret, mask = cv2.threshold(img, 127, 255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)

# create a mask
#mask = np.zeros(thresh.shape[:2], np.uint8)
#mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)
'''
color = ('b','g','r')
# 对一个列表或数组既要遍历索引又要遍历元素时
# 使用内置enumerrate 函数会有更加直接，优美的做法
#enumerate 会将数组或列表组成一个索引序列。
# 使我们再获取索引和索引内容的时候更加方便
for i,col in enumerate(color):
         histr = cv2.calcHist([img],[i],None,[256],[0,256])
         plt.plot(histr,color = col)
         plt.xlim([0,256])
plt.show()
'''




cv2.imshow('masked_img', masked_img)

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()

