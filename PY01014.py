

if __name__=='__main__':
    a,k,n=map(int,input().split())
    b_min=(int((a/k))+1)*k-a
    b_max=(int(n/k))*k-a
    if b_min<=b_max:
        for i in range(b_min,b_max+1,k):
            print(i,end=' ')
    else:
        print(-1)

