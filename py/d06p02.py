from d06lib import read_d06
from collections import Counter

groups = read_d06()
total = 0
for g in groups:
    counter = Counter("".join(g))
    total += len([ans for (ans, cnt) in counter.items() if cnt == len(g)])
print(total)
