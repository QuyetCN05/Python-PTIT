from collections import *
from functools import *
from math import *
import io, os, sys, time
from datetime import datetime


class Items:
    def __init__(self, id, name, amount, price, discount) -> None:
        self.__id = id
        self.__name = name
        self.__amount = amount
        self.__price = price
        self.__discount = discount

    def get_total(self):
        return self.__amount * self.__price - self.__discount

    def __str__(self) -> str:
        return f"{self.__id} {self.__name} {self.__amount} {self.__price} {self.__discount} {self.get_total()}"


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        id = input()
        name = input()
        amount = int(input())
        price = int(input())
        discount = int(input())
        x = Items(id, name, amount, price, discount)
        arr.append(x)
    arr.sort(key=lambda x: (-x.get_total()))
    for x in arr:
        print(x)
