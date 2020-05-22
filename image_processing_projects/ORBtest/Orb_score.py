# This time, we will use BFMatcher.knnMatch() to get k best matches. 
# In this example, we will take k=2 so that we can apply ratio test 
# explained by D.Lowe in his paper. 

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img1= cv.imread('1.PNG', cv.IMREAD_GRAYSCALE)          # queryImage
img2 = cv.imread('4-1canny(40,100).png', cv.IMREAD_GRAYSCALE) # trainImage

method = 'ORB'  # 'SIFT'
lowe_ratio = 0.89
magic_number =0.99
if method   == 'ORB':
    finder = cv.ORB_create()
elif method == 'SIFT':
    finder = cv.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = finder.detectAndCompute(img1,None)
kp2, des2 = finder.detectAndCompute(img2,None)

# BFMatcher with default params
bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []

for m,n in matches:
    if m.distance < lowe_ratio*n.distance:
        good.append([m])

msg1 = 'using %s with lowe_ratio %.2f' % (method, lowe_ratio)
msg2 = 'there are %d good matches' % (len(good))

img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good, None, flags=2)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img3,msg1,(10, 250), font, 0.5,(255,255,255),1,cv.LINE_AA)
cv.putText(img3,msg2,(10, 270), font, 0.5,(255,255,255),1,cv.LINE_AA)
fname = 'output_%s_%.2f.png' % (method, magic_number)
cv.imwrite(fname, img3)

plt.imshow(img3),plt.show()