import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img= [cv2.imread('QuickSave Merge 20180705_175133.tif',0),cv2.imread('QuickSave Merge 20180703_172255.tif',0),cv2.imread('QuickSave Merge 20180703_172257.tif',0),cv2.imread('QuickSave Merge 20180703_172300.tif',0),cv2.imread('QuickSave Merge 20180705_175129.tif',0),cv2.imread('QuickSave Merge 20180705_175131tif',0)]


# global thresholding
for i in range(0,6):
    ret1, th1 = cv2.threshold(img[i], 200, 255, cv2.THRESH_BINARY)

    ret2, th2 = cv2.threshold(img[i], 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    blur = cv2.GaussianBlur(img[i],(5,5),0)

    ret3, th3 = cv2.threshold(img[i], 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plot all the images and their histograms
    images = [img, 0, th1, img, 0, th2, blur, 0, th3]

    titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)', 'Original Noisy Image','Histogram',"Otsu's Thresholding", 'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

    #for i in xrange(3):
	 #   plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
	  #  plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
	    #plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
	    #plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
	    #plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
	    #plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
    
    plt.plot(),plt.imshow(images[8],'gray')
    plt.axis('off')
    plt.show()
    #fig=plt.figure()
    #fig.savefig()
"""
for j in range(0,6):
    for i in xrange(3):
	    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
	    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
	    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
	    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
	    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
	    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

plt.show()
"""