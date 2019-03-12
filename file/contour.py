import cv2

def edge_detect(file_name, tresh_min, tresh_max):
    image = cv2.imread(file_name)
    im_bw = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    (thresh, im_bw) = cv2.threshold(im_bw, tresh_min, tresh_max, 0)
    cv2.imwrite('bw_'+file_name, im_bw)

    contours, hierarchy = cv2.findContours(im_bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0,255,0), 3)
    cv2.imwrite('cnt_'+file_name, image)

if __name__ == '__main__':
  edge_detect('/Users/William/opencv/venv/file/testpics/9.jpeg', 128, 255)
