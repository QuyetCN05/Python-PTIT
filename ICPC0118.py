from math import *

t = int(input())
i = 1
while i <= t:
    a, b = map(int, input().split())
    s = b*100+a
    if (s >= 321 and s <= 419):
        print('Bach Duong')
    elif (s >= 420 and s <= 520):
        print('Kim Nguu')
    elif (s >= 521 and s <= 620):
        print('Song Tu')
    elif (s >= 621 and s <= 722):
        print('Cu Giai')
    elif (s >= 723 and s <= 822):
        print('Su Tu')
    elif (s >= 823 and s <= 922):
        print('Xu Nu')
    elif (s >= 923 and s <= 1022):
        print('Thien Binh')
    elif (s >= 1023 and s <= 1122):
        print('Thien Yet')
    elif (s >= 1123 and s <= 1221):
        print('Nhan Ma')
    elif (s >= 1222 or s <= 119):
        print('Ma Ket')
    elif (s >= 120 and s <= 218):
        print('Bao Binh')
    elif (s >= 219 and s <= 320):
        print('Song Ngu')
    i += 1
