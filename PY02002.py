


   
 

if __name__=='__main__':
    t=int(input())
    while t !=0:
        t-=1
        c,d=map(int,input().split())
        a=[1]*93
        for i in range(3,93):
            a[i]=a[i-1]+a[i-2]
        for i in range(c,d+1):
            print(a[i],end=' ')
        print()
        
       

    
       
    
