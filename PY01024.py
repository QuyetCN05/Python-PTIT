from math import *
def check(s):
    a=list(s)
    for i in range(0,len(a)-1):
        if(abs(int(a[i])-int(a[i+1])) != 2):
            return False
    
    return True

def tong(s):
    a=list(s)
    sum=0

    for i in a:
        sum+=int(i)

    return(sum%10==0)

if __name__=='__main__':
    for i in range(int(input())):
        s=input()
        if(check(s) and tong(s)):
            print('YES')
        else:
            print('NO')
