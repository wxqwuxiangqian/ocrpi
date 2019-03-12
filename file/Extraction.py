import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import pytesseract

oimg = cv2.imread('/Users/William/opencv/venv/file/testpics/text.jpeg') #读取图片
img = cv2.cvtColor(oimg,cv2.COLOR_RGB2GRAY) #调为灰度图片
img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
img = cv2.blur(img,(5,5))

kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])
kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],[-1,2,2,2,-1],[-1,2,8,2,-1],[-1,2,2,2,-1],[-1,-1,-1,-1,-1]]) / 8.0

output_1 = cv2.filter2D(img, -1, kernel_sharpen_1)
output_2 = cv2.filter2D(img, -1, kernel_sharpen_2)
output_3 = cv2.filter2D(img, -1, kernel_sharpen_3)

#cv2.imshow('Edge Enhancement', output_3)
#cv2.waitKey(0)

img = output_3

#cv2.imshow('Grayscale', gray_img)
#cv2.waitKey(0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
ret,thresh6 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

ret,thresh6 = cv2.threshold(thresh3,127,255,cv2.THRESH_BINARY)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

histeq = cv2.equalizeHist(thresh3)

#text = pytesseract.image_to_string(thresh1, )
#data = pytesseract.image_to_data(thresh1, lang='eng')

#print(text)


#with open('text.txt','w') as f:
#    f.write(text)


cv2.imshow('thresh3',thresh6)


cv2.waitKey(0)
#for i in range(6):
 #   plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
  #  plt.title(titles[i])
   # plt.xticks([]),plt.yticks([])

#plt.show()

