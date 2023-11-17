from math import *
from decimal import *


class Point:
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    def distance(self, other):
        ans = sqrt((self.__x-other.__x)**2+(self.__y-other.__y)**2)
        return ans


class Triangle:
    def __init__(self, p1, p2, p3) -> None:
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3

    def peimeter(self):
        a = self.__p1.distance(self.__p2)
        b = self.__p1.distance(self.__p3)
        c = self.__p2.distance(self.__p3)
        if  (max(a, b, c) * 2 >= a + b + c):
            print('INVALID')
        else:
            d = sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4
            print('{:.2f}'.format(d))

if __name__ == '__main__':
    a = []
t = int(input())
for x in range(t):
    a += [float(i) for i in input().split()]
i = 0
for index in range(t):
    triagle = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
    triagle.peimeter()
    i += 6