a=int(input())
b= int(input())
c=int(input())
d=b**2-4*a*c
if d>0:
    x1=(-b+d**0.5)/2*a
    x2=(-b-d**0.5)/2*a
    print(x1,x2)
if d==0:
    x1=-b/2*a
    print(x1)
if d<0:
    print('net korney')