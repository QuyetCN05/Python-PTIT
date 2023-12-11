from itertools import *
from math import *
from collections import *
from functools import *

if __name__=='__main__':
    arr=[]
    for i in range(int(input())):
        cmp=''
        s=input()
        s+='?'
        for j in range(len(s)):
            if s[j] >='0' and s[j] <='9':
                cmp+=s[j]
            else:
                if cmp !='':
                    arr.append(int(cmp))
                cmp=''
    arr.sort()
    for j in arr:
        print(j)

