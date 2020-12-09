from collections import deque
from itertools import combinations


def read_d09(filename="../inputs/d09-input.txt"):
    values = []
    with open(filename) as f:
        for l in f:
            values.append(int(l))
    return values


def get_weakness():
    values = deque(read_d09())
    preamble_length = 25
    buffer = deque(maxlen=preamble_length)
    while len(buffer) < preamble_length:
        buffer.append(values.popleft())
    while values:
        val = values.popleft()
        if not any(a + b == val for (a, b) in combinations(buffer, 2)):
            return val
        buffer.append(val)
