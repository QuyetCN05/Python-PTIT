from math import *

def check(s):
    for i in range(2,len(s),2):
        if s[i] != s[i-2]:
            return False
    
    return True
def check_2(s):
    return(s[0]!=s[1])
if __name__=='__main__':
    for i in range(int(input())):
        s=input()
        if((len(s)%2==1) and check(s) and check_2(s)):
            print('YES')
        else:
            print('NO')
