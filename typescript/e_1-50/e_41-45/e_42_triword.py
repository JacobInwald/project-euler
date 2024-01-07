import math as m 
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../'))
from utils import *

def alpha_pos(c: str) -> int:
    """
    Returns the position of a letter in the alphabet.
    
    Parameters:
        c (str): The letter whose position is to be determined.
        
    Returns:
        int: The position of the letter in the alphabet. Returns 0 if the input is not a letter.
    """
    if c.lower() not in "abcdefghijklmnopqrstuvwxyz":
        return 0
    return ord(c.lower()) - 96
    

def isTriWord(w: str) -> bool:
    """
    Determines if a word is a triangular word.
    
    A word is considered a triangular word if the sum of the positions of its letters in the alphabet is a triangular number.
    
    Args:
        w (str): The word to check.
        
    Returns:
        bool: True if the word is a triangular word, False otherwise.
    """
    sum = 0
    for c in w:
        sum += alpha_pos(c)
    return is_tri(sum)


with open(os.path.join(os.path.dirname(__file__), '../../../data/words.txt'), 'r') as f:
    words = f.readline().split(',')

count = 0
for w in words:
    if isTriWord(w):
        count+=1

print(count)

