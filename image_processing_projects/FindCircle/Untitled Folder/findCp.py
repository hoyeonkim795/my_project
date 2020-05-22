from sympy import Symbol, solve
#import math
new_md=[] 

dot=[[6,2],[1,7],[3,6],[5,4]] #(x-1)^2 + (y-2)^2=25
A=Symbol('A')
B=Symbol('B')
C=Symbol('C')
for i in range(0,len(dot)-2):
   for j in range(i+1,len(dot)-1):
        for k in range(j+1,len(dot)):
           a=dot[i]
           b=dot[j]
           c=dot[k]
           #print(a,b,c)
           x1=a[0]
           y1=a[1]
           eq=x**2+A*x+y**2+B*y+C
           eq1=eq
           #print(eq1)
           x=b[0]
           y=b[1]
           eq=x**2+A*x+y**2+B*y+C
           eq2=eq
           #print(eq2)
           x=c[0]
           y=c[1]
           eq=x**2+A*x+y**2+B*y+C
           eq3=eq
           #print(eq3)
           result = solve((eq1,eq2,eq3),dict=True)
           print(result)
           if len(result) > 0:
               result = result[0]
               result_A = result[A]
               result_B = result[B]
               result_C = result[B]
               mx= result_A
               my= result_B
               mz= result_C
               md = [mx, my,mz]

               new_md.append(md)
#print(new_md)
'''for l in range (0,len(new_md)):
   for p in range(l,len(new_md)):
       if l==p:
           break
       else:
           new_md[l]==new_md[p]
           print(l,new_md[l])'''