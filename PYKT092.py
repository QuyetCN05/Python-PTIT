from math import *

from functools import *

# def cmp(a,b):
#     if a.get_diem_xt() != b.get_diem_xt():
#         return b.get_diem_xt()-a.get_diem_xt()
#     else:
#         if a.get_ma() <b.get_ma():
#             return -1
#         else:
#             return 1
class Student:
    def __init__(self,ma,ten,diem,dan_toc,khu_vuc) -> None:
        self.__ma=ma
        self.__ten=ten
        self.__diem=diem
        self.__dan_toc=dan_toc
        self.__khu_vuc=khu_vuc
    def get_ma(self):
        return self.__ma
    def get_diem_xt(self):
        ans=self.__diem
        if self.__khu_vuc==1:
            ans+=1.5
        elif self.__khu_vuc==2:
            ans+=1.0
        else:
            ans+=0
        if self.__dan_toc=='Kinh':
            ans+=0
        else:
            ans+=1.5
        return ans
    def normally(self):
        a=self.__ten.split()
        self.__ten=' '.join(a).title()
    def get_status(self):
        if self.get_diem_xt()>=20.5:
            return 'Do'
        else:
            return 'Truot'
    def __str__(self) -> str:
        return f'{self.__ma} {self.__ten} {self.get_diem_xt()} {self.get_status()}'
if __name__=='__main__':
    n=int(input())
    arr=[]
    for i in range(1,n+1):
        ma='TS%02d'%(i)
        ten=input()
        diem=float(input())
        dan_toc=input().strip()
        khu_vuc=int(input())
        p=Student(ma,ten,diem,dan_toc,khu_vuc)
        p.normally()
        arr.append(p)
    arr.sort(key=lambda x:(-x.get_diem_xt()))
    # arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)
        

