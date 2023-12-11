from collections import *
from functools import *
from math import *
import io, os, sys, time
from datetime import datetime

class Employee:
    def __init__(self,id,name,salary,day,department) -> None:
        self.__id=id
        self.__name=name
        self.__salary=salary
        self.__day=day
        self.__department=department
    
    def get_paychecks(self):
        sum=0
        sum=self.__salary*self.__day*(10**3)
        if self.__id[0]=='A':
            if int(self.__id[1:3]) >=1 and int(self.__id[1:3]) <=3:
                sum*=10
            elif int(self.__id[1:3]) >=4 and int(self.__id[1:3]) <=8:
                sum*=12
            elif int(self.__id[1:3]) >=9 and int(self.__id[1:3]) <=15:
                sum*=14
            else:
                sum*=20
        elif self.__id[0]=='B':
            if int(self.__id[1:3]) >=1 and int(self.__id[1:3]) <=3:
                sum*=10
            elif int(self.__id[1:3]) >=4 and int(self.__id[1:3]) <=8:
                sum*=11
            elif int(self.__id[1:3]) >=9 and int(self.__id[1:3]) <=15:
                sum*=13
            else:
                sum*=26
        elif self.__id[0]=='C':
            if int(self.__id[1:3]) >=1 and int(self.__id[1:3]) <=3:
                sum*=9
            elif int(self.__id[1:3]) >=4 and int(self.__id[1:3]) <=8:
                sum*=10
            elif int(self.__id[1:3]) >=9 and int(self.__id[1:3]) <=15:
                sum*=12
            else:
                sum*=14
        else:
            if int(self.__id[1:3]) >=1 and int(self.__id[1:3]) <=3:
                sum*=8
            elif int(self.__id[1:3]) >=4 and int(self.__id[1:3]) <=8:
                sum*=9
            elif int(self.__id[1:3]) >=9 and int(self.__id[1:3]) <=15:
                sum*=11
            else:
                sum*=13
        
        return sum

            
    
    def __str__(self) -> str:
        return f'{self.__id} {self.__name} {self.__department} {self.get_paychecks()}'
    

if __name__=='__main__':
    arr,d=[],dict()
    n=int(input())
    for i in range(n):
        s=input()
        a=s.split()
        d[a[0]]=' '.join(a[1:])
    m=int(input())
    for i in range(m):
        id=input()
        name=input()
        salary=int(input())
        day=int(input())
        s=Employee(id,name,salary,day,d[id[3:]])
        arr.append(s)
    for x in arr:
        print(x)


