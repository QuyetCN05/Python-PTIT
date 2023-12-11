from collections import *
from functools import *
from math import *
import io, os, sys, time
from datetime import datetime


def cmp(a, b):
    date1, date2 = a.get_day().split("/"), b.get_day().split("/")
    if date1[-1] != date2[-1]:
        return int(date1[-1]) - int(date2[-1])
    if date1[-2] != date2[-2]:
        return int(date1[-2]) - int(date2[-2])
    if date1[-3] != date2[-3]:
        return int(date1[-3]) - int(date2[-3])
    hour1, hour2 = a.get_hour().split(":"), b.get_hour().split(":")
    if hour1[0] != hour2[0]:
        return int(hour1[0]) - int(hour2[0])
    if hour1[1] != hour2[1]:
        return int(hour1[1]) - int(hour2[1])
    return a.get_code() < b.get_code()


class Schedule:
    def __init__(self, name, id, code, day, hour, kip) -> None:
        self.__name = name
        self.__id = id
        self.__code = code
        self.__day = day
        self.__hour = hour
        self.__kip = kip

    def get_id(self):
        return self.__id

    def get_code(self):
        return self.__code

    def get_day(self):
        return self.__day

    def get_hour(self):
        return self.__hour

    def get_kip(self):
        return self.__kip

    def set_name(self, name):
        self.__name = name

    def __str__(self) -> str:
        return f"{self.__id} {self.__code} {self.__name} {self.__day} {self.__hour} {self.__kip}"


if __name__ == "__main__":
    t, n = map(int, input().split())
    d = dict()
    arr = []
    for i in range(t):
        x = input()
        y = input()
        d[x] = y
    a = list(d.keys())
    for i in range(1, n + 1):
        id = "T%03d" % (i)
        s = list(input().split())
        sv = Schedule(d[s[0]], id, s[0], s[1], s[2], s[3])
        arr.append(sv)
    arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)
