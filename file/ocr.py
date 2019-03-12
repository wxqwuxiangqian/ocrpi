import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import pytesseract

oimg = cv2.imread('/Users/William/opencv/venv/file/testpics/text.jpeg') #读取图片
img = cv2.cvtColor(oimg,cv2.COLOR_RGB2GRAY) #调为灰度图片

#增强锐度
kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],[-1,2,2,2,-1],[-1,2,8,2,-1],[-1,2,2,2,-1],[-1,-1,-1,-1,-1]]) / 8.0
output_3 = cv2.filter2D(img, -1, kernel_sharpen_3)

#图片近似黑白化
ret,thresh1 = cv2.threshold(output_3,127,255,cv2.THRESH_BINARY)

# 用tesseract识别数字
text = pytesseract.image_to_string(thresh1, lang='eng')

print(text)

#写入文件
with open('text.txt','w') as f:
    f.write(text)


cv2.imshow('thresh1',thresh1)

cv2.waitKey(0)
#for i in range(6):
#    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])

#plt.show()

