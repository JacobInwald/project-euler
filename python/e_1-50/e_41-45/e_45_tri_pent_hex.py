# Import parent library
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

for i in range(1, 100000):
    t = gen_tri(i)
    if is_pent(t) and is_hex(t):
        print(i,t)