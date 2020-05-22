import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/kriskim/Documents/Python/gaussian/puf.tif',0)
img1 =  cv2.imread('/home/kriskim/Documents/Python/gaussian/puf.tif')
# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#############################################################
os_img = th3   

os_img = cv2.medianBlur(os_img,5)
cimg = cv2.cvtColor(os_img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(os_img,cv2.HOUGH_GRADIENT,1,150,
                            param1=80,param2=50,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    x = i[0]  
    y = i[1]
    r = i[2]
######################################
height,width = img.shape
mask = np.zeros((height,width), np.uint8)
cv2.circle(mask,(x,y),z,(255,255,255),thickness=-1)
masked_data = cv2.bitwise_and(cimg, cimg, mask=mask)
_,thresh = cv2.threshold(mask,1,255,cv2.THRESH_BINARY)
contours = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
x,y,w,h = cv2.boundingRect(contours[0])
crop = masked_data[y:y+h,x:x+w]
##############################3#######
cv2.imshow('detected circles',crop)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('/home/kriskim/Documents/Python/FindCircle/circled_eye.png',cimg)
    cv2.destroyAllWindows()