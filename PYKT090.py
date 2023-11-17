from math import *
from functools import *
from collections import *
if __name__ == '__main__':
    f = open('CONTACT.in', 'r')
    b = set()
    for line in f:
        if line[-1] == '\n':
            b.add(line[:-1].lower())
        else:
            b.add(line.lower())

    a = list(b)
    a.sort()
    for x in a:
        print(x)
