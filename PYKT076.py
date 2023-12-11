from collections import *
from functools import *
from math import *
import io, os, sys, time
from datetime import datetime


def cmp(a, b):
    c, d = list(a.get_day().split("/")), list(b.get_day().split("/"))
    if c[-1] != d[-1]:
        return int(c[-1]) - int(d[-1])
    if c[-2] != d[-2]:
        return int(c[-2]) - int(d[-2])
    if c[-3] != d[-3]:
        return int(c[-3]) - int(d[-3])
    if a.get_name() != b.get_name():
        if a.get_name() < b.get_name():
            return -1
        else:
            return 1
    else:
        return b.get_episode() - a.get_episode()


class Film:
    def __init__(self, id, category, day, name, episode) -> None:
        self.__id = id
        self.__category = category
        self.__day = day
        self.__name = name
        self.__episode = episode

    def get_day(self):
        return self.__day

    def get_name(self):
        return self.__name

    def get_episode(self):
        return self.__episode

    def __str__(self) -> str:
        return (
            f"{self.__id} {self.__category} {self.__day} {self.__name} {self.__episode}"
        )


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr, d = [], dict()
    for i in range(1, n + 1):
        s = input()
        id = "TL%03d" % (i)
        d[id] = s
    for i in range(1, m + 1):
        id = "P%03d" % (i)
        code = input()
        day = input()
        name = input()
        episode = int(input())
        sv = Film(id, d[code], day, name, episode)
        arr.append(sv)
    arr.sort(key=cmp_to_key(cmp))
    for x in arr:
        print(x)
