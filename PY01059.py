
def check(s):
    a=list(s)
    for i in range(len(a)):
        if i%2==1 and a[i] !='0':
            return False
    
    return True
if __name__=='__main__':
    for i in range(int(input())):
        s=input()
        a=list(s)
        sum_1,tich_1=0,1
        for i in range(len(a)):
            if i%2==0:
                sum_1+=int(a[i])
            else:
                if a[i] !='0':
                    tich_1*=int(a[i])
                else:
                    continue
        if check(s):
            print(sum_1,0,sep=' ')
        else:
            print(sum_1,tich_1,sep=' ')