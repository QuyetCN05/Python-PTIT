from math import *
from functools import *


def cmp(a, b):
    if b.get_ma() > a.get_ma():
        return -1
    else:
        return 1


class Exam:
    def __init__(self, ma, mon, ht) -> None:
        self.__ma = ma
        self.__mon = mon
        self.__ht = ht

    def get_ma(self):
        return self.__ma

    def __str__(self) -> str:
        return f'{self.__ma} {self.__mon} {self.__ht}'


if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(1, n+1):
        ma = input()
        mon = input()
        ht = input()
        p = Exam(ma, mon, ht)
        a.append(p)
    a.sort(key=cmp_to_key(cmp))
    for x in a:
        print(x)
