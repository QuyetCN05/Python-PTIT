from math import *
for i in range(int(input())):
    n=int(input())
    a=str((3+sqrt(5))**n)
    b=a.index('.')
    if b>=3:
        print('Case #',i+1,': ',a[b-3:b:1],sep='')
    else:
        print('Case #',i+1,': ','0'+a[0:b],sep='')
