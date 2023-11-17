from math import *
from functools import *


class Student:
    def __init__(self, ma, ten, diem_1, diem_2, diem_3) -> None:
        self.__ma = 'SV{:02d}'.format(ma)
        self.__ten = ten
        self.__diem_1 = diem_1
        self.__diem_2 = diem_2
        self.__diem_3 = diem_3
      

   

    def normally(self):
        a = self.__ten.split()
        self.__ten = ' '.join(a).title()

    def get_ma(self):
        return self.__ma

    def get_diem(self):
        ans = self.__diem_1*3+self.__diem_2*3+self.__diem_3*2
        return ans/8

    def __str__(self) -> str:
        return f'{self.__ma} {self.__ten} {ceil(self.get_diem()*100)/100} {self.rank}'



n = int(input())
arr = []
for i in range(1, n+1):
    ten = input().strip()
    diem_1 = int(input())
    diem_2 = int(input())
    diem_3 = int(input())
    p = Student(i, ten, diem_1, diem_2, diem_3)
    p.normally()
    arr.append(p)
arr.sort(key=lambda x: (-x.get_diem(), x.get_ma()))
arr[0].rank=1
for i in range(1, len(arr)):
    arr[i].rank = arr[i-1].rank if arr[i].get_diem() == arr[i-1].get_diem() else i + 1
for x in arr:
    print(x)

    
