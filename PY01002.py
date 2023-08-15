from math import *

s=input()
a=[]
for i in s:
    if(i.isdigit()):
        a.append(i)
if(int(a[0])+int(a[1])==int(a[2])):
    print("YES")
else:
    print('NO')