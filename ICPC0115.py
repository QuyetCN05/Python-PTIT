from math import *
if __name__=='__main__':
    for i in range(int(input())):
        s=input()
        a=list(s)
        sum=0
        for i in range(0,len(a)):
            sum+=factorial(int(a[i]))
        if(sum==int(s)):
            print('Yes')
        else:
            print('No')