from collections import *
from functools import *
from math import *
import io, os, sys, time
from datetime import datetime


class Employee:
    def __init__(self, code, name, id, last, current) -> None:
        self.__code = code
        self.__name = name
        self.__id = id
        self.__last = last
        self.__current = current

    def get_fee(self):
        sum = 0
        if self.__id == "A":
            if self.__current - self.__last < 100:
                sum = (self.__current - self.__last) * 450
            else:
                sum = 100 * 450
        elif self.__id == "C":
            if self.__current - self.__last < 200:
                sum = (self.__current - self.__last) * 450
            else:
                sum = 200 * 450
        else:
            if self.__current - self.__last < 500:
                sum = (self.__current - self.__last) * 450
            else:
                sum = 500 * 450
        return sum

    def get_tax(self):
        res = 0
        if self.__id == "A":
            if self.__current - self.__last <= 100:
                res = 0
            else:
                res = (self.__current - self.__last - 100) * 1000
        elif self.__id == "C":
            if self.__current - self.__last <= 200:
                res = 0
            else:
                res = (self.__current - self.__last - 200) * 1000
        else:
            if self.__current - self.__last <= 500:
                res = 0
            else:
                res = (self.__current - self.__last - 500) * 1000
        return res

    def get_vat(self):
        return self.get_tax() // 20

    def get_total(self):
        return self.get_fee() + self.get_tax() + self.get_vat()

    def __str__(self) -> str:
        return f"{self.__code} {self.__name} {self.get_fee()} {self.get_tax()} {self.get_vat()} {self.get_total()}"


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(1, n + 1):
        code = "KH%02d" % (i)
        name = input().strip().split()
        str = input().split()
        x = Employee(code, " ".join(name).title(), str[0], int(str[1]), int(str[2]))
        arr.append(x)
    arr.sort(key=lambda x: -x.get_total())
    for x in arr:
        print(x)
