import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

divisors = [i for i in range(1,21)]

for i in range(20,1000000000, 20):
    if all([(i // d) * d == i for d in divisors]):
        print(i)
        break