from math import *
import io, os, sys, time
import array as arr

class Team:
    def __init__(self,id,name,school) -> None:
        self.__id=id
        self.__name=name
        self.__school=school
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_school(self):
        return self.__school

class Student:
    def __init__(self,id,name,teamCode,school,teamName) -> None:
        self.__id=id
        self.__name=name
        self.__teamCode=teamCode
        self.__school=school
        self.__teamName=teamName
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_teamCode(self):
        return self.__teamCode
    def get_school(self):
        return self.__school
    def set_school(self,school):
        self.__school=school
    def set_teamName(self,teamName):
        self.__teamName=teamName
    def __str__(self) -> str:
        return f'{self.__id} {self.__name} {self.__teamName} {self.__school}'
        

if __name__=='__main__':
    n=int(input())
    arr=[]
    for i in range(1,n+1):
        code='Team%02d'%(i)
        name=input()
        school=input()
        x=Team(code,name,school)
        arr.append(x)
    m=int(input())
    b=[]
    for i in range(1,m+1):
        id='C%03d'%(i)
        name=input()
        teamCode=input()
        x=Student(id,name,teamCode,' ',' ')
        for y in arr:
            if y.get_id()==x.get_teamCode():
                x.set_school(y.get_school())
                x.set_teamName(y.get_name())
        b.append(x)
    b.sort(key=lambda x:(x.get_name()))
    for x in b:
        print(x)

        



