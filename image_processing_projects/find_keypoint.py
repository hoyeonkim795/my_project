import numpy as np
import cv2
import math
from matplotlib import pyplot as plt

img = cv2.imread('made_1_1.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,40,0.2,5)#두번째가 
corners = np.int0(corners)
cd=[]
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
    cd.append([x,y]) 
    
print(cd[0])
print(cd[1])

center = [230,230]
a = cd[0][0]
b = cd[0][1]
firstpoint = [a,b]
info = []
print(cd)
print(len(cd))
for i in range(len(cd)):
   length = int(math.sqrt(math.pow((cd[i][0]-center[0]),2) + math.pow((cd[i][1]-center[1]),2))) 
   cos = 0
   info.append([length,cos])
print (info)


plt.imshow(img),plt.show()
[[250,250]]