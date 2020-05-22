import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img= [cv2.imread('/home/kriskim/Documents/Python/gaussian/puf.tif',0)]
# img = cv2.medianBlur(img,5)
for i in range(0,3):
	ret, th1 = cv2.threshold(img[i],127,255,cv2.THRESH_BINARY)



	th2 = cv2.adaptiveThreshold(img[i],255,cv2.ADAPTIVE_THRESH_MEAN_C,\
	cv2.THRESH_BINARY,15,2)
	th3 = cv2.adaptiveThreshold(img[i],255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
	cv2.THRESH_BINARY,15,2)

	#titles = ['Original','Global','Mean','Gaussian']

	images = [img,th1,th2,th3]


	plt.figure(i+1)
	plt.plot(),plt.imshow(images[2],'gray')
	plt.axis('off')
	plt.show()