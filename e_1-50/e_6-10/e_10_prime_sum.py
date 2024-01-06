import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

print(sum(sieve_of_eratosthenese(2000000)))