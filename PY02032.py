from collections import *
from functools import *
from math import *


if __name__=='__main__':
    s=input()
    if len(s) %2==0:
        a=list(s)
        
        arr=[]
        for i in range(0,len(a),2):
            ans=int(a[i]+a[i+1])
            arr.append(ans)
        
        b=list(set(arr))
        b.sort()
        for j in b:
            print(j,end=' ')
    else:
        a=list(s)
        
        arr=[]
        for i in range(0,len(a)-1,2):
            ans=int(a[i]+a[i+1])
            arr.append(ans)
        
        b=list(set(arr))
        b.sort()
        for j in b:
            print(j,end=' ')
    

