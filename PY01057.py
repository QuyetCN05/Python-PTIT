
from math import *

def nt(n):
    if n <2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    
    return True

def check(s):
    for i in range(len(s)):
        if (nt(i) and not(nt(int(s[i])))) or(not(nt(i)) and nt(int(s[i]))):
            return 'NO'
        
    return 'YES'

if __name__=='__main__':
    for i in range(int(input())):
        s=input()
        print(check(s))
        