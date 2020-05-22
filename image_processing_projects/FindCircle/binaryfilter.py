
import cv2
import numpy as np
from matplotlib import pyplot as plt


class PUF:
    def setdata(self, x, y, r, img):
        self.x = x#self 는 circ 를 의미
        self.y = y 
        self.r = r
        self.img = img
    def findCp (self,img,x,y,r) :
        a = self.findTp(img,x,y,r)
        b = self.findBp(img,x,y,r)
        vector1 = np.array(a)
        vector2 = np.array(b)
        vector3 = np.array(self.findLp(img,x,y,r))
        vector4 = np.array(self.findRp(img,x,y,r))
        sum_vector = vector1 + vector2 +vector3 + vector4
        c = int((b[1]-a[1])/2)
        self.x = int(sum_vector[0]/4)
        self.y = int(sum_vector[1]/4)
        self.r = c
        

    def findTp (self,img,x,y,r) :
        xcor = 10
        ycor = 10
        while xcor > 0 :
            if img[xcor,ycor] == 0: 
                if pow(xcor-x,2) + pow(ycor-y,2) > 0.95*pow(r,2):
                    if xcor<490 :
                        xcor = xcor+1
                        continue
                    else :
                        xcor = 10
                        ycor = ycor + 1
                        continue
                else:
                    print(xcor,ycor,img[xcor,ycor])
                    return ([xcor,ycor])
                    break
            elif xcor<490 :
                xcor = xcor+1
            else :
                xcor = 10
                ycor = ycor + 1
    def findBp (self,img,x,y,r) :
        xcor = 490
        ycor = 490
        while xcor > 0 :
            if img[xcor,ycor] == 0: 
                if pow(xcor-x,2) + pow(ycor-y,2) > 0.95*pow(r,2):
                    if xcor > 10 :
                        xcor = xcor - 1
                        continue
                    else :
                        xcor = 490
                        ycor = ycor - 1
                        continue
                else:
                    print(xcor,ycor,img[xcor,ycor])
                    return ([xcor,ycor])
                    break
            elif xcor > 10 :
                xcor = xcor - 1
            else :
                xcor = 490
                ycor = ycor - 1
    def findLp (self,img,x,y,r) :
        xcor = 10
        ycor = 10
        while xcor > 0 :
            if img[xcor,ycor] == 0: 
                if pow(xcor-x,2) + pow(ycor-y,2) > 0.95*pow(r,2):
                    if ycor<490 :
                        ycor = ycor+1
                        continue
                    else :
                        ycor = 10
                        xcor = xcor + 1
                        continue
                else:
                    print(xcor,ycor,img[xcor,ycor])
                    return ([xcor,ycor])
                    break
            elif ycor<490 :
                ycor = ycor+1
            else :
                ycor = 10
                xcor = xcor + 1
    def findRp (self,img,x,y,r) :
        xcor = 490
        ycor = 490
        while xcor > 0 :
            if img[xcor,ycor] == 0: 
                if pow(xcor-x,2) + pow(ycor-y,2) > 0.95*pow(r,2):
                    if ycor > 10 :
                        ycor = ycor - 1
                        continue
                    else :
                        ycor = 490
                        xcor = xcor - 1
                        continue
                else:
                    print(xcor,ycor,img[xcor,ycor])
                    return ([xcor,ycor])
                    break
            elif ycor > 10 :
                ycor = ycor - 1
            else :
                ycor = 490
                xcor = xcor - 1
    def drawcircle(self,img):
        self.findCp(img,250,250,300)
        cv2.circle(img,(self.x,self.y),2,(0,255,0),3)#cv2.circle(img, center, radian, color, thickness)
        cv2.circle(img,(self.x,self.y),self.r,(35,56,56),3)
        print(self.x,self.y,self.r)
#if pow(xcor,2) + pow(ycor,2) > pow(r,2):
                   

img = cv2.imread('made_1_1.png',0)
ret,thresh1 = cv2.threshold(img,170,255,cv2.THRESH_BINARY)
'''
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
'''
titles = ['Original Image','BINARY']
images = [img, thresh1]
print(thresh1[10,10])

'''
while xcor > 0 :
    if thresh1[xcor,ycor] == 0: 
        print(xcor,ycor,thresh1[xcor,ycor])
        break
    elif xcor<490 :
        xcor = xcor+1
    else :
        xcor = 10
        ycor = ycor + 1
'''
PUF1 = PUF()
PUF1.drawcircle(thresh1)


for i in range(2):
    #plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.subplot(1,2,i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()