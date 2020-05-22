import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/kriskim/Documents/Python/pictures/4-3.PNG',0)


kernel = np.ones((5,5),np.uint8)
kernel2 = np.ones((3,3),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 4)
opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
gaus = cv2.GaussianBlur(erosion,(5,5),0)
median = cv2.medianBlur(erosion,1)
bila = cv2.bilateralFilter(opening,11,75,75)
dilation = cv2.dilate(bila,kernel2,iterations = 4)
gradient = cv2.morphologyEx(bila, cv2.MORPH_GRADIENT, kernel)
#blurring
gaus = cv2.GaussianBlur(erosion,(5,5),0)
median = cv2.medianBlur(erosion,1)
bila = cv2.bilateralFilter(img,9,75,75)

#####################################################
#Thresh holding
gausth = cv2.adaptiveThreshold(gradient,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2) #adaptive gaussian
mean = cv2.adaptiveThreshold(gradient,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)# adaptive mean
ret,otsu = cv2.threshold(gradient,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#################################################################################3  
# molphological
kernel = np.ones((5,5),np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
erosion = cv2.erode(img,kernel,iterations = 1)
opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mean, cv2.MORPH_CLOSE, kernel)
dilation = cv2.dilate(img,kernel,iterations = 1)
########################################################3
#image gradients
lapla = cv2.Laplacian(median,cv2.CV_64F)

###
#canny edge
cv2.imshow('kak',closing)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('/home/kriskim/Documents/Python/FindCircle/circled_eye.png',gausth)
    cv2.destroyAllWindows()