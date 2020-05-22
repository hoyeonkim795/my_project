import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('/home/kriskim/Documents/Python/gaussian/puf.tif',0)
# global thresholding
ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# Otsu's thresholding
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
#blur = cv.GaussianBlur(img,(5,5,0)
#blur = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
#cv.THRESH_BINARY,15,2)
blur = cv.bilateralFilter(img,6,2,2)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# plot all the images and their histograms
images = [img, 0, th1, img, 0, th2, blur, 0, th3]

titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)', 'Original Noisy Image','Histogram',"Otsu's Thresholding", 'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
#############################################################
os_img = images[8]   
#plt.plot(),plt.imshow(images[8],'gray')
#plt.axis('off')
#plt.show()
os_img = cv.medianBlur(os_img,5)
cimg = cv.cvtColor(os_img,cv.COLOR_GRAY2BGR)

circles = cv.HoughCircles(os_img,cv.HOUGH_GRADIENT,1,150,
                            param1=10,param2=40,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv.imshow('detected circles',cimg)
k = cv.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('/home/kriskim/Documents/Python/FindCircle/circled_eye.png',cimg)
    cv.destroyAllWindows()