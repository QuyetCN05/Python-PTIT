from collections import *
from functools import *
from math import *
import pickle 
import io
import os
import sys
import time

def check(n):
    res=n%10
    n //=10
    while n !=0:
        a=n%10
        if a > res:
            return False
        res=a
        n //=10
    return True


if __name__=='__main__':
    arr,brr=[],[]
    set_1,set_2=set(),set()
    with open('DATA2.in','rb') as p:
        try:
           arr=pickle.load(p)
        except EOFError:
            arr=[]
    
        
    dic_1,dic_2={},{}
   
    with  open('DATA3.in','rb') as file:
            try:
               brr=pickle.load(file)
            except EOFError:
                brr=[]
      

    for x in arr:
        if check(int(x)):
            set_1.add(x)
            if x in dic_1:
                dic_1[x]+=1
            else:
                dic_1[x]=1
    for x in brr:
        if check(int(x)):
            set_2.add(x)
            if x in dic_2:
                dic_2[x]+=1
            else:
                dic_2[x]=1
    u= set_1 & set_2
    c=list(u)
    c.sort()
    for j in c:
        print(j,dic_1[j],dic_2[j],sep=' ')
    # print(check(1134))
    
    

 
    