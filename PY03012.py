from math import *
from functools import *


def cmp(a, b):
    if a.get_ac() != b.get_ac():
        return b.get_ac()-a.get_ac()
    elif a.get_submit() != b.get_submit():
        return a.get_submit()-b.get_submit()
    else:
        if a.get_ten() < b.get_ten():
            return -1
        else:
            return 1


class Student:
    def __init__(self, ten, ac, submit) -> None:
        self.__ten = ten
        self.__ac = ac
        self.__submit = submit

    def get_ten(self):
        return self.__ten

    def get_ac(self):
        return self.__ac

    def get_submit(self):
        return self.__submit

    def __str__(self) -> str:
        return f'{self.__ten} {self.__ac} {self.__submit}'


if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(1, n+1):
        ten = input()
        b, c = map(int, input().split())
        p = Student(ten, b, c)
        a.append(p)
    a.sort(key=cmp_to_key(cmp))
    for x in a:
        print(x)
