import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

print(max(prime_factorize(600851475143)))