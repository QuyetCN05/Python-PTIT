from collections import *

if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        check = False
        b = n/2
        res = Counter(a)
        for i in res.keys():
            if res[i] > b:
                print(i)
                check = True
                break
        if check == False:
            print('NO')
