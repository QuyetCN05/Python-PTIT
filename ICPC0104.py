t=int(input())

for i in range(1,t+1):
    s=input()
    sum=0
    num=0
    for j in s:
        if(j.isdigit()):
            num=num*10+(int(j)-0)
        else:
            sum=max(num,sum)
            num=0
    sum=max(num,sum)
    print(sum)