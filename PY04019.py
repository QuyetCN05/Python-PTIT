from math import *
from functools import *

def cmp(a,b):
    if a.get_diem_tb() >b.get_diem_tb():
        return -1
    else:
        return 1
class Student:
    def __init__(self,ma,ten,diem_1,diem_2) -> None:
        self.__ma=ma
        self.__ten=ten
        self.__diem_1=diem_1
        self.__diem_2=diem_2
    def get_diem_tb(self):
        if self.__diem_1>10:
            self.__diem_1=self.__diem_1/10
        else:
            self.__diem_1=self.__diem_1/1.0
        if self.__diem_2 >10:
            self.__diem_2=self.__diem_2/10
        else:
            self.__diem_2=self.__diem_2/1.0
        sum=(self.__diem_1+self.__diem_2)/2
        return sum
    def get_xep_loai(self):
        if self.get_diem_tb() >9.5:
            return 'XUAT SAC'
        elif self.get_diem_tb() >=8:
            return 'DAT'
        elif self.get_diem_tb() >=5:
            return 'CAN NHAC'
        else:
            return 'TRUOT'
    def __str__(self) -> str:
        return f'{self.__ma} {self.__ten} {self.get_diem_tb():.2f} {self.get_xep_loai()}'
if __name__=='__main__':
    n=int(input())
    a=[]
    for i in range(1,n+1):
        ma='TS0'+str(i)
        ten=input()
        lt, th = float(input()), float(input())
        p=Student(ma,ten,lt,th)
        a.append(p)
    a.sort(key=lambda Student:-Student.get_diem_tb())
    for x in a:
        print(x)
    
