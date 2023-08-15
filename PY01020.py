from math import *

if __name__=='__main__':
    t=int(input())
    for i in range(1,t+1):
        s=input()
        str='86'
        tmp=s[len(s)-2]+s[len(s)-1]
        if(tmp==str):
            print('YES')
        else:
            print('NO')