import cv2
import numpy as np
import random
import math
def distan(a,b,x,y):
    return math.sqrt((pow((a-x),2)+(pow((b-y),2))))

def drawrandomcircle(img, num,x,y,r):
    cv2.circle(img,(x,y),2,(255,0,0),3)
    cv2.circle(img,(x,y),r,(0,255,0),3)
    while num > 0:
        rnum1 = random.randrange(0,450)-x#첫번째 원의 중점을 원점으로한 좌표로 변환
        rnum2 = -(random.randrange(0,450)-y)#첫번째 원의 중점을 원점으로한 좌표로 변환
        print (rnum1, rnum2)
        if(pow(rnum1,2) + pow(rnum2,2) < pow(r,2) ) & (distan(rnum1,rnum2,0,0)<(r*1/3)):#1이하 0이상으로 곱해저야함, 2/3이하 추천, 작으면 작을수록 내부 원이 커짐
            rr = random.randrange(int(0.7*(r-distan(rnum1,rnum2,0,0))),int(r-distan(rnum1,rnum2,0,0)))
            cv2.circle(img,(rnum1+x,y-rnum2),2,(255,255,0),3)#출력시에는 다시 원래의 좌표계로 변환해줘야함
            cv2.circle(img,(rnum1+x,y-rnum2),rr,(255,255,0),3)#0.7최소 원반지름 크면 클수록 큰원나옴
            break
        #if(num > 0):
            #drawrandomcircle(img, num-1,rnum1+x,y-rnum2,rr)
    cv2.imshow('detected circles',img)


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
print(j,x,y)

drawrandomcircle(cimg,3, x,y,200)


k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('/home/kriskim/Documents/Python/FindCircle/circled_eye.png',cimg)
    cv2.destroyAllWindows()