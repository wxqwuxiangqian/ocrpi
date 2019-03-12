import cv2
import numpy as np
from matplotlib import pyplot as plt

oimg = cv2.imread('/Users/William/opencv/venv/file/testpics/4.jpeg') #读取图片
img = cv2.cvtColor(oimg,cv2.COLOR_RGB2GRAY) #调为灰度图片


kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])
kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],[-1,2,2,2,-1],[-1,2,8,2,-1],[-1,2,2,2,-1],[-1,-1,-1,-1,-1]]) / 8.0

output_1 = cv2.filter2D(img, -1, kernel_sharpen_1)
output_2 = cv2.filter2D(img, -1, kernel_sharpen_2)
output_3 = cv2.filter2D(img, -1, kernel_sharpen_3)


cv2.imshow('Edge Enhancement', output_3)
cv2.waitKey(0)