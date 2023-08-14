import math
t=int(input())
while t>0 :
    a,b,c=map(float,input().split())
    cnt=c/a
    print(math.ceil(math.log(cnt,(1+b/100))))
    t-=1


