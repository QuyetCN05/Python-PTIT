from math import *


def check(s):
    str = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(str[i])-ord(str[i-1])):
            return False
    
    return True


if __name__ == '__main__':
    for i in range(int(input())):
        s = input()
        if check(s):
            print('YES')
        else:
            print('NO')
