from math import *
from functools import *
from collections import *

def cmp(a,b):
    if a.get_gio() != b.get_gio():
        return b.get_gio() -a.get_gio()
    else:
        return b.get_phut()-a.get_phut()
class Time:
    def __init__(self,ma,ten,gio,phut) -> None:
        self.__ma=ma
        self.__ten=ten
        self.__gio=gio
        self.__phut=phut
    def get_gio(self):
        return self.__gio
    def get_phut(self):
        return self.__phut
    def __str__(self) -> str:
        return f'{self.__ma} {self.__ten} {self.__gio} gio {self.__phut} phut'
if __name__=='__main__':
    n=int(input())
    a=[]
    for i in range(1,n+1):
        ma=input()
        ten=input()
        vao=input()
        ra=input()
        res,ans=0,0
        gio_1,phut_1=int(vao[0:2]),int(vao[3:5])
        gio_2,phut_2=int(ra[0:2]),int(ra[3:5])
        if phut_2 >=phut_1:
            res=gio_2-gio_1
            ans=phut_2-phut_1
        else:
            res=gio_2-gio_1-1
            ans=60+phut_2-phut_1
        p=Time(ma,ten,res,ans)
        a.append(p)
    a.sort(key=cmp_to_key(cmp))
    for x in a:
        print(x)
    

    