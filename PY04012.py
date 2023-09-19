from math import *

from functools import *

class Student:
    def __init__(self,ma,ten,lop,diem_danh) -> None:
        self.__ma=ma
        self.__ten=ten
        self.__lop=lop
        self.__diem_danh=diem_danh
    def set_diem_danh(self,res):
        self.__diem_danh=res
    def get_ma(self):
        return self.__ma
    def get_diem(self):
        res=10
        a=list(self.__diem_danh)
        b=a.count('m')
        c=a.count('v')
        res=res-b*1-c*2
        if res <=0:
            return 0
        else:
            return res
    def get_xep_loai(self):
        if self.get_diem()==0:
            return 'KDDK'
    def __str__(self) -> str:
        if self.get_diem() ==0:
            return f'{self.__ma} {self.__ten} {self.__lop} {self.get_diem()} {self.get_xep_loai()}'
        else:
            return f'{self.__ma} {self.__ten} {self.__lop} {self.get_diem()}'
if __name__=='__main__':
    n=int(input())
    arr=[]
    for i in range(1,n+1):
        ma=input()
        ten=input()
        lop=input()
        p=Student(ma,ten,lop,'')
        arr.append(p)
    for i in range(1,n+1):
        tmp,st=input().split()
        for x in arr:
            if x.get_ma()==tmp:
                x.set_diem_danh(st)
    for x in arr:
        print(x)






    

        