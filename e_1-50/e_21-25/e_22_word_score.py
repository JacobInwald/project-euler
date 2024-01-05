import os

def score(name: str) -> int:
    return sum(ord(c) - 64 for c in name)

with open(os.path.join(os.path.dirname(__file__), '../../data/names.txt')) as f:
    names = f.read().replace('"', '').split(',')
    names.sort()

print(sum(score(names[i])*(i+1) for i in range(len(names))))

