from math import *
from functools import *
from collections import *

if __name__=='__main__':
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    count=[0]*600
    for x in a:
        count[x]+=1
    max_1=max_2=-10**4
    for so in count:
        if so > max_1:
            max_2 = max_1
            max_1 = so
        elif so > max_2 and so != max_1:
            max_2 = so
    
    if max_2==0:
        print('NONE')
    else:
        
        for j in range(len(count)):
            if count[j]==max_2:
                print(j)
                break
