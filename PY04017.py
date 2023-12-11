from collections import *
from functools import *
from math import *
import io, os, sys, time
from datetime import datetime

def cmp(a,b):
    return b.get_speed()-a.get_speed()

class Athlete:
    def __init__(self,name,address,speed) -> None:
        self.__id=id
        self.__name=name
        self.__address=address
        self.__speed=speed
    def get_speed(self):
        return self.__speed
    
    def normally(self):
        a=list(self.__address.split())
        str=''
        for x in a:
            str+=x[0]
        b=list(self.__name.split())
        for x in b:
            str+=x[0]
        self.__id=str
            
    
    def __str__(self) -> str:
        return f"{self.__id} {self.__name} {self.__address} {round(self.__speed)} Km/h"
    

if __name__=='__main__':
    format = "%H:%M"
    start="6:00"
    arr=[]
    n=int(input())
    for i in range(n):
        name=input()
        address=input()
        finish=input()
        time_start = datetime.strptime(start, format)
        time_finish = datetime.strptime(finish, format)
        y = (time_finish - time_start).total_seconds() / 3600
        speed=120/y
        sv=Athlete(name,address,speed)
        sv.normally()
        arr.append(sv)
    
    arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)
    
        
        
