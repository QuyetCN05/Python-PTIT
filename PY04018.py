from math import *
from functools import *



class Lecture:
    def __init__(self,ma,ten,recruit,tin,sub) -> None:
        self.__ma=ma
        self.__ten=ten
        self.__recruit=recruit
        self.__tin=tin
        self.__sub=sub
    def get_diem(self):
        ans=self.__tin*2+self.__sub
        if self.__recruit[1]=='1':
            ans+=2.0
        elif self.__recruit[1]=='2':
            ans+=1.5
        elif self.__recruit[1]=='3':
            ans+=1.0
        else:
            ans+=0
        return ans
    def get_mon(self):
        if self.__recruit[0]=='A':
            return 'TOAN'
        elif self.__recruit[0]=='B':
            return 'LY'
        else:
            return 'HOA'
    def get_xep_loai(self):
        if self.get_diem() >=18:
            return 'TRUNG TUYEN'
        else:
            return 'LOAI'
    def __str__(self) -> str:
        return f'{self.__ma} {self.__ten} {self.get_mon()} {self.get_diem():.1f} {self.get_xep_loai()}'
if __name__=='__main__':
    n=int(input())
    a=[]
    for i in range(1,n+1):
        ma='GV%02d' %(i)
        ten=input()
        recruit=input()
        tin=float(input())
        sub=float(input())
        p=Lecture(ma,ten,recruit,tin,sub)
        a.append(p)
    a.sort(key=lambda x:-x.get_diem())
    for x in a:
        print(x)
