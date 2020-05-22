#a = [[209.3624641833811, 211.3624641833811, 163.00775820866062], [182, 212.69117647058823, 80.35440663765719], [249.3881118881119, 249.3881118881119, 199.45665846076116], [-54.76470588235294, -54.76470588235294, 554.6769532722172], [101.12724014336918, 101.12724014336918, 408.094905303836], [249.5, 249.5, 350.017856687341]]

import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)
def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] >= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result
#def changetoangle(cos,apoint):


coc1 = [[200,250,250],[155, 277, 256],[114,262,270],[81,262,245]]
coc2 = [200, 253,249],[258,276]
point1 = [[305, 440],[250, 51],[409, 131],[90, 369],[440, 196],[131, 409],[60, 305],[90, 131]]
point2 = [[273,52],[421,153],[432,328],[392,388],[112,393],[53,227],[67,174],[106,113]]
sort_coc =merge_sort (coc1)
#print(sort_coc)
cx1=sort_coc[0][1] #원의 중점 좌표
#print(cx1)
cy1=sort_coc[0][2]
#print(cy1)
cx2=sort_coc[1][1] #원의 중점 좌표
#print(cx2)
cy2=sort_coc[1][2]
#print(cy2)

angle1=[]
for [x1,y1] in point1:
    try:
        xx=int(math.degrees(math.atan2(-(y1-cy1),(x1-cx1))-math.atan2(-(cy2-cy1),(cx2-cx1))))
        if(xx<0):
            xx=xx+360
        angle1.append (xx)
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
sortangle1 =merge_sort (angle1)
print(sortangle1)

cx1=253 #원의 중점 좌표
#print(cx1)
cy1=249
#print(cy1)
cx2= 261#원의 중점 좌표
#print(cx2)
cy2=276.38
#268256, 258276,268229
angle2=[]
for [x1,y1] in point2:
    try:
        xx=int(math.degrees(math.atan2(-(y1-cy1),(x1-cx1))-math.atan2(-(cy2-cy1),(cx2-cx1))))
        if(xx<0):
            xx=xx+360
        angle2.append (xx)
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
sortangle2 =merge_sort (angle2)
print(sortangle2)
x=[0,0]
y=[27,-6]
x_1=(y[0]-x[0])*math.cos(-(3.141592)/3)-(y[1]-x[1])*math.sin(-(3.141592)/3)
y_1=(y[0]-x[0])*math.sin(-(3.141592)/3)+(y[1]-x[1])*math.cos(-(3.141592)/3)
print(x_1+250,(-y_1)+250)
#print (math.degrees(math.atan(3.45)))
#print(180*math.atan(440-250/305-250)/3.14)#-math.atan(256-250/277-250))

#중점좌표를 다빼줘야함

#angle = math.atan(x)(y1*x2-x1*y2 / x1*x2+y1*y2)
'''
img = cv2.imread('white.jpg',0)   
cv2.circle(img,(209,211),163,(0,255,0),3)
cv2.circle(img,(182,212),80,(0,255,0),3)
cv2.circle(img,(250,250),200,(0,200,0),3)
cv2.imshow('detected circles',img)   

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    #cv2.imwrite('/home/kriskim/Documents/Python/FindCircle/circled_eye.png',cimg)
    cv2.destroyAllWindows()
'''