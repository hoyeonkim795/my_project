import cv2
import numpy as np
import random
import math

img = cv2.imread('made7.png',0)
print (img.size)
px = img[115,102]
print (px)

cv2.imshow('detected circles',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('/home/kriskim/Documents/Python/FindCircle/circled_eye.png',cimg)
    cv2.destroyAllWindows()