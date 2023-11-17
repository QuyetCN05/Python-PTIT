from collections import *
from functools import *
from math import *
import io, os, sys, time
from datetime import datetime




# datetime_str = ' 3:55:0'
# start=' 8:30:0'
# datetime_object = datetime.strptime(datetime_str, ' %H:%M:%S')
# datetime_sv = datetime.strptime(start, ' %H:%M:%S')


# print((datetime_sv-datetime_object).total_seconds())


class Rain:
    def __init__(self,id,name) -> None:
        self.__id=id
        self.__name=name
        self.__amount=[]
        self.__time=[]
    def caculate(self,x,y):
        self.__amount.append(x)
        self.__time.append(y)
    def __str__(self) -> str:
        return f'{self.__id} {self.__name} {sum(self.__amount)/sum(self.__time):.2f}'


if __name__=='__main__':
    format='%H:%M'
    n=int(input())
    b=set()
    a=dict()
    arr=[]
    cnt=0
    for i in range(1,n+1):
        name=input()
        start=input()
        finish=input()
        amount=int(input())
        if name not in b:
            cnt+=1
            id='T%02d'%(cnt)
            x=Rain(id,name)
            b.add(name)
            time_start=datetime.strptime(start,format)
            time_finish=datetime.strptime(finish,format)
            y=(time_finish-time_start).total_seconds()/3600
            x.caculate(amount,y)
            arr.append(x)
            a[name]=x
        else:
            x=a.get(name)
            time_start=datetime.strptime(start,format)
            time_finish=datetime.strptime(finish,format)
            y=(time_finish-time_start).total_seconds()/3600
            x.caculate(amount,y)
    for x in arr:
        print(x)
  


        
