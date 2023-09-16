from math import *
from functools import *


def cmp(a, b):
    if a.get_diem_tb() > b.get_diem_tb():
        return -1
    else:
        return 1


class Student:
    def __init__(self, ma, ten,
                 toan, tv, anh, li, hoa, sinh, su, dia,
                 cd, cn) -> None:
        self.__ma = ma
        self.__ten = ten
        self.__toan = toan
        self.__tv = tv
        self.__anh = anh
        self.__li = li
        self.__hoa = hoa
        self.__sinh = sinh
        self.__su = su
        self.__dia = dia
        self.__cd = cd
        self.__cn = cn

    def get_diem_tb(self):
        sum = (self.__toan*2+self.__tv*2+self.__anh+self.__li+self.__hoa+self.__sinh+self.__su
               + self.__dia+self.__cd+self.__cn)/12
        return sum

    def get_xep_loai(self):
        if self.get_diem_tb() >= 9:
            return 'XUAT SAC'
        elif self.get_diem_tb() >= 8:
            return 'GIOI'
        elif self.get_diem_tb() >= 7:
            return 'KHA'
        elif self.get_diem_tb() >= 5:
            return 'TB'
        else:
            return 'YEU'

    def __str__(self) -> str:
        return f'{self.__ma} {self.__ten} {round(self.get_diem_tb(),1)} {self.get_xep_loai()}'


if __name__ == '__main__':
    a = []
    n = int(input())
    for i in range(1, n+1):
        ma = 'HS%02d' % (i)
        ten = input()
        t, b, c, d, e, f, g, h, j, k = map(float, input().split())
        p = Student(ma, ten, t, b, c, d, e, f, g, h, j, k)
        a.append(p)
    a.sort(key=cmp_to_key(cmp))
    for x in a:
        print(x)
