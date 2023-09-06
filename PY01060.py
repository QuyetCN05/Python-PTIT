

def check(s):
    a=list(s)
    for i in range(len(a)):
        if i%2==0 and a[i] !='0':
            return False
    
    return True

if __name__=='__main__':
    for i in range(int(input())):
        s=input()
        a=list(s)
        sum,tich=0,1
        for i in range(len(a)):
            if i%2==0:
                if a[i] !='0':
                    tich*=int(a[i])
                else:
                    continue
            else:
                sum+=int(a[i])
        if check(s):
            print(0,sum,sep=' ')
        else:
            print(tich,sum,sep=' ')