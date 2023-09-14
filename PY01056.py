from math import *


def nt(n):
    if n<2:
        return False
    
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    
    return True
def check_1(n):
    for i in range(0,len(n),2):
        if int(n[i])%2==1:
            return False
    
    return True

def check_2(s):
    for i in range(1,len(s),2):
        if int(s[i])%2==0:
            return False
    
    return True

if __name__=='__main__':

    for i in range(int(input())):
        s=input()
        sum=0
        for j in s:
            sum+=int(j)
        if nt(sum) and check_1(s) and check_2(s):
            print('YES')
        else:
            print('NO')
       

    

