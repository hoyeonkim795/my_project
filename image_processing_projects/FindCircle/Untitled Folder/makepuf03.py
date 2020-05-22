import cv2
import numpy as np
import random
import math

class circ:
    thick = 2#선굵기
    numberofcircle = 0
    degree = 0
    
    def setdata(self, x, y, r, img):
        self.x = x#self 는 circ 를 의미
        self.y = y 
        self.r = r
        self.img = img
        
    def distan(self,a,b,x,y):
        return math.sqrt((pow((a-x),2)+(pow((b-y),2))))#두점 사이의 거리 공 식
    def findPointOnCirc(self,x,y,r,dg):#원점 좌표와 반지름 넣어서 그 위의 랜던한 점 하나 반환
        th = math.radians(circ.degree)
        rnumx = r*math.cos(th)
        rnumy = r*math.sin(th)
        circ.degree = circ.degree + dg
        return int(rnumx+x),int(y-rnumy)
             
    def findIntersect(self,x,y,r):# 점의 좌표, 반지름,
        interx = x*r/self.distan(0,0,x,y)
        intery = y*r/self.distan(0,0,x,y)
        return int(interx), int(intery) 
    def drawlines(self,img,x1,y1,r,num,x2,y2,rr):#실제좌표를 입력으로 받음
        cimg = img
        dg = 360/num
        circ.degree = circ.degree+random.randrange(0,360)
        while num > 0:
            a,b = self.findPointOnCirc(x1,y1,r,dg)#Out 원위의 랜덤한점 실제좌표 을 찾음 
            interx,intery = self.findIntersect(a-x2,-(b-y2),rr) #inner원에 대한 상대좌표 입력
            cv2.line(cimg, (interx+x2,y2-intery), (a,b) , (0,255,0), circ.thick)#실제좌표 변환
            #cv2.line(cimg, (x2,y2), (a,b) , (0,255,0), 3) #실제좌표 변환
            num = num-1 
            if(num == 0): 
                return cimg
            else: continue


    def drawcircle(self,img,x,y,r,dr):
        cv2.circle(img,(x,y),2,(255,0,0),circ.thick)#cv2.circle(img, center, radian, color, thickness)
        cv2.circle(img,(x,y),r,(0,255,0),circ.thick)
        rr = r-dr
        self.x = x #다음원 중점의 x좌표
        self.y = y #다음원 중점의 y좌표
        self.r = rr#다음원의 반지름
        self.img = img
        if(circ.numberofcircle == 5):
            return
        else:
            circ.numberofcircle = circ.numberofcircle+1
            img = self.drawlines(img,x,y,r,10,x,y,rr)#실제 좌표 입력
            
dr = 40
cimg = cv2.imread('white.jpg',0)
circ1 = circ()
circ2 = circ()
circ3 = circ()
circ4 = circ()
circ5 = circ()
circ6 = circ()
circ1.drawcircle(cimg,250,250,250,dr) 
circ2.drawcircle(circ1.img,circ1.x,circ1.y,circ1.r,dr)
circ3.drawcircle(circ2.img,circ2.x,circ2.y,circ2.r,dr)
circ4.drawcircle(circ3.img,circ3.x,circ3.y,circ3.r,dr)
circ5.drawcircle(circ4.img,circ4.x,circ4.y,circ4.r,dr)
circ6.drawcircle(circ5.img,circ5.x,circ5.y,circ5.r,dr)


cv2.imshow('detected circles',circ3.img)   

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('/home/kriskim/Documents/Python/FindCircle/circled_eye.png',cimg)
    cv2.destroyAllWindows()