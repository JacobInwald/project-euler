# Import parent library
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

def isPanMultiple(n):
    mag_order = len(str(n))
    for i in range(1, mag_order+1):
        str_check = ""
        for mul in range(1, i+1):
            str_check += str(n*mul)
        if isPan(int(str_check)):
            return int(str_check)
    return 0

max = 0
for i in range(0,1000000):
    if isPanMultiple(i) > max:
        print(i, isPanMultiple(i))