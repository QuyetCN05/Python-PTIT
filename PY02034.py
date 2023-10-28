from collections import *
from functools import *
from math import *


if __name__=='__main__':
    s=input()
    if len(s) %2==0:
        a=list(s)
        
        d,arr={},[]
        for i in range(0,len(a),2):
            ans=int(a[i]+a[i+1])
            arr.append(ans)
        
        b=[]
        for x in arr:
            if x not in d:
                b.append(x)
                d[x]=1
        se=dict.fromkeys(b,0)
        for x in arr:
            if x in se:
                se[x]+=1
            else:
                se[x]=1
        for j in se:
            print(j,se[j],sep=' ')
    else:
        a=list(s)
        
        d,arr={},[]
        for i in range(0,len(a)-1,2):
            ans=int(a[i]+a[i+1])
            arr.append(ans)
        
        b=[]
        for x in arr:
            if x not in d:
                b.append(x)
                d[x]=1
        se=dict.fromkeys(b,0)
        for x in arr:
            if x in se:
                se[x]+=1
            else:
                se[x]=1
        for j in se:
            print(j,se[j],sep=' ')
    

