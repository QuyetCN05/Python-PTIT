

if __name__=='__main__':
    t=int(input())
    while t !=0:
        t-=1
        s=input()
        res=1
        for i in s:
            if int(i) !=0:
                res*=int(i)
        print(res)
