def check(n):
    a = n
    sum = 0
    while n != 0:
        sum = sum*10+n % 10
        n //= 10
    return (a == sum)


if __name__ == '__main__':
    t = int(input())
    while t != 0:
        t-=1
        s = input()
        sum = 0
        for i in s:
            sum += int(i)
        if(sum >9 and check(sum)):
            print('YES')
        else:
            print('NO')
         
        

