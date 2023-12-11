from functools import *
from collections import *
import os,sys,io,time
from math import*

if __name__=='__main__':
    s=input()
    if len(s)%3==1:
        s='00'+s
    elif len(s)%3==2:
        s='0'+s
    result=''
    for i in range(0,len(s),3):
        result+=str(int(s[i:i+3],2))
    print(result)
    # print(str(int(s[0:3],2)))

    
    

