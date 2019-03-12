import cv2
import numpy as np
from matplotlib import pyplot as plt

oimg = cv2.imread('/Users/William/opencv/venv/file/testpics/4.jpeg') #读取图片
img = cv2.cvtColor(oimg,cv2.COLOR_RGB2GRAY) #调为灰度图片
#cv2.imshow('Grayscale', gray_img)
#cv2.waitKey(0)
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
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