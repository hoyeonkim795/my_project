import cv2
import numpy as np
import random
import math

class circ:
    thick = 2#선굵기
    def setdata(self, x, y, r, img):
        self.x = x#self 는 circ 를 의미
        self.y = y 
        self.r = r
        self.img = img
        
    def distan(self,a,b,x,y):
        return math.sqrt((pow((a-x),2)+(pow((b-y),2))))#두점 사이의 거리 공 식
    def findPointOnCirc(self,x,y,r):#원점 좌표와 반지름 넣어서 그 위의 랜던한 점 하나 반환
        while x > 0:
            rnum1 = random.randrange(0,450)-x#첫번째 원의 중점을 원점으로한 좌표로 변환
            rnum2 = -(random.randrange(0,450)-y)#첫번째 원의 중점을 원점으로한 좌표로 변환
            if(pow(rnum1,2) + pow(rnum2,2) == pow(r,2)):
                return rnum1+x,y-rnum2
    def findIntersect(self,x,y,r):# 점의 좌표, 반지름,
        interx = x*r/self.distan(0,0,x,y)
        intery = y*r/self.distan(0,0,x,y)
        return int(interx), int(intery) 
    def drawlines(self,img,x1,y1,r,num,x2,y2,rr):#실제좌표를 입력으로 받음
        cimg = img
        while num > 0:
            a,b = self.findPointOnCirc(x1,y1,r)#Out 원위의 랜덤한점 실제좌표 을 찾음 
            interx,intery = self.findIntersect(a-x2,-(b-y2),rr) #inner원에 대한 상대좌표 입력
            cv2.line(cimg, (interx+x2,y2-intery), (a,b) , (0,255,0), circ.thick)#실제좌표 변환
            #cv2.line(cimg, (x2,y2), (a,b) , (0,255,0), 3) #실제좌표 변환
            num = num-1 
            if(num == 0): 
                return cimg


    def drawcircle(self,img,x,y,r):
        cv2.circle(img,(x,y),2,(255,0,0),circ.thick)#cv2.circle(img, center, radian, color, thickness)
        cv2.circle(img,(x,y),r,(0,255,0),circ.thick)
        while x > 0:  
            rnum1 = random.randrange(0,450)-x#out원의 중점을 원점으로한 inner원 중점의 상대 좌표
            rnum2 = -(random.randrange(0,450)-y)# 파이썬 출력 y축이 반대임
            #a,b = self.findPointOnCirc(x,y,r)
            #print (rnum1, rnum2)
            if(pow(rnum1,2) + pow(rnum2,2) < pow(r,2) ) & (self.distan(rnum1,rnum2,0,0)<(r*1/5)):#1이하 0이상으로 곱해저야함, 2/3이하 추천, 작으면 작을수록 내부 원이 커짐
                rr = random.randrange(int(0.7*(r-self.distan(rnum1,rnum2,0,0))),int(r-self.distan(rnum1,rnum2,0,0))) #반지름 설정
                cv2.circle(img,(rnum1+x,y-rnum2),2,(255,0,0),circ.thick)#출력시에는 다시 원래의 좌표계로 변환해줘야함
                cv2.circle(img,(rnum1+x,y-rnum2),rr,(0,255,0),circ.thick)#0.7최소 원반지름 크면 클수록 큰원나옴
                print(rr)
                #cv2.circle(img,(rnum1+x,y-rnum2),2,(random.randrange(0,256),random.randrange(0,256),random.randrange(0,256)),3)#랜덤색
                #cv2.circle(img,(rnum1+x,y-rnum2),rr,(random.randrange(0,256),random.randrange(0,256),random.randrange(0,256)),3)#랜덤색
                img = self.drawlines(img,x,y,r,10,rnum1+x,y-rnum2,rr)#실제 좌표 입력 선개수선개수
                self.x = rnum1+x #다음원 중점의 x좌표
                self.y = y-rnum2 #다음원 중점의 y좌표
                self.r = rr#다음원의 반지름
                self.img = img
                print(self.x)
                print(self.y)
                
                #cv2.line(img, (rnum1+x,y-rnum2), (a,b), (0,255,0), 3)
                break



'''
img = cv2.imread('1-1.PNG',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,
                            param1=50,param2=100,minRadius=0,maxRadius=0)
j = 0
x = 0
y = 0
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    j+=1
    
    #cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    #cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    x+=i[0]
    y+=i[0]
x = (int(x/j))
y = (int(y/j)) 
print(j,x,y)#원엄청 그려서 중점 평균 찾기
'''

cimg = cv2.imread('white.jpg',0)
circ1 = circ()
circ2 = circ()
circ3 = circ()
circ4 = circ()
circ5 = circ()
circ1.drawcircle(cimg,250,250,200) 
circ2.drawcircle(circ1.img,circ1.x,circ1.y,circ1.r)
circ3.drawcircle(circ2.img,circ2.x,circ2.y,circ2.r)
circ4.drawcircle(circ3.img,circ3.x,circ3.y,circ3.r)
circ5.drawcircle(circ4.img,circ4.x,circ4.y,circ4.r)

cv2.imshow('detected circles',circ3.img)   

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    #cv2.imwrite('/home/kriskim/Documents/Python/FindCircle/circled_eye.png',cimg)
    cv2.destroyAllWindows()