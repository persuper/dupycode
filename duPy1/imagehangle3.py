import cv2
import numpy as np

e1 = cv2.getTickCount()

img1=cv2.imread('e:/ducap.png')
#图像尺寸
sz1 = img1.shape[0] #height(rows) of image
sz2 = img1.shape[1] #width(colums) of image
sz3 = img1.shape[2] #the pixels value is made up of three primary colors

#创建空白图像
mask = np.zeros(img1.shape,np.uint8)

#添加文字内容
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(mask,'dujianjun',(10,100), font, 4,(255,0,0),2)

#img3 = np.zeros(img1.shape,np.unit8) # (sz2,sz1,1),np.uint8)

#图像融合一下看啊看
dst=cv2.addWeighted(img1,0.7,mask,0.3,0)
cv2.imshow('dst',dst)

#output text image



cv2.imwrite('e:/imageweight.png', dst)

text = np.zeros((200,300,3) ,np.uint8)
cv2.putText(text,'dujianjun',(10,50), font, 2,(0,0,255),2)
cv2.imwrite('e:/text.png', text)


# 图像尺寸
rows,cols,channels = img1.shape
roi = np.zeros(img1.shape, np.uint8)

cv2.putText(roi,'dujianjun',(10,50), font, 2,(0,0,255),2)


# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

cv2.imshow("mask", mask_inv)

# Now black-out the area of logo in ROI
# 取roi 中与mask 中不为零的值对应的像素的值，其他值为0
# 注意这里必须有mask=mask 或者mask=mask_inv, 其中的mask= 不能忽略
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
# 取roi 中与mask_inv 中不为零的值对应的像素的值，其他值为0。
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img1,img1,mask = mask_inv)



# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('res',img1)

e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print("程序执行时间为：")
print(t)



cv2.waitKey(0)
cv2.destroyAllWindows()





cv2.waitKey(0)
#cv2.destroyAllWindow()
