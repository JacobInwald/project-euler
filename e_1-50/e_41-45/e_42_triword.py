import os
import math as m 
# t = 0.5n(n+1)
# 2t = n^2 + n
def alpha_pos(c):
    if c.lower() not in "abcdefghijklmnopqrstuvwxyz":
        return 0
    return ord(c.lower()) - 96

def isTriNum(t):
    return m.sqrt(8*t + 1) % 1 == 0

def isTriWord(w):
    sum = 0
    for c in w:
        sum += alpha_pos(c)
    return isTriNum(sum)

with open(os.path.join(os.path.dirname(__file__), 'data/words.txt'), 'r') as f:
    words = f.readline().split(',')

count = 0
for w in words:
    if isTriWord(w):
        count+=1

print(count)

