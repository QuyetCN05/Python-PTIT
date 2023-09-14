from collections import *

def check(s):
    for i in range(2,len(s)):
        if s[i] !=s[i-2]:
            return False
    
    return True
if __name__=='__main__':
    for i in range(int(input())):
        s=input()
        a=list(s)
        b= set(a)
        if check(s) and len(b)==2:
            print('YES')
        else:
            print('NO')
