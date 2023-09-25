from math import *
from collections import *
from itertools import *
from functools import *

class Team:
    def __init__(self,id,ten,truong) -> None:
        self.__id='Team%02d' %(id)
        self.__ten=ten
        self.__truong=truong
    def get_id(self):
        return self.__id
    def get_ten(self):
        return self.__ten
    def get_truong(self):
        return self.__truong

class Student:
    def __init__(self,ma,name,doi,school) -> None:
        self.__ma='C%03d' %(ma)
        self.__name=name
        self.__doi=doi
        self.__school=school
    def get_ma(self):
        return self.__ma
    def get_name(self):
        return self.__name
    def get_doi(self):
        return self.__doi
    def get_school(self):
        return self.__school
    def __str__(self) -> str:
        return f'{self.__ma} {self.__name} {self.__doi} {self.__school}'


if __name__=='__main__':
    n=int(input())
    a=[]
    for i in range(1,n+1):
        ten=input()
        truong=input()
        p=Team(i,ten,truong)
        a.append(p)
    m=int(input())
    arr=[]
    for i in range(1,m+1):
        name=input()
        doi=input()
        for x in a:
            if x.get_id()==doi:
                sv=Student(i,name,x.get_ten(),x.get_truong())
                arr.append(sv)
    arr.sort(key=lambda x: x.get_name())
    for x in arr:
        print(x)



        