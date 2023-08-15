from math import *

t = int(input())
for i in range(1,t+1):
    s=input()
    str=''
    for j in range(0,len(s)):
        if(j==2):
            break
        str+=s[j]

    vt=s[len(s)-2]+s[len(s)-1]
    if(vt==str):
        print('YES')
    else:
        print('NO')
        

   
   
