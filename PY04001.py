from math import *
from decimal import *


class Point:
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    def distance(self, other):
        ans= sqrt((self.__x-other.__x)**2+(self.__y-other.__y)**2)
        return '{:.4f}'.format(ans)


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
