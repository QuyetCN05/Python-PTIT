from functools import *
from itertools import *
from collections import *


arr=[('English',88),('Science',90),('Math',97),('Social Science',82)]
arr.sort(key=lambda x: x[1])
print(arr)
# for x in arr:
#     print(x)