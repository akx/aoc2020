from collections import deque
from itertools import product, combinations

from d09lib import read_d09


def main():
    values = deque(read_d09())
    preamble_length = 25
    buffer = deque(maxlen=preamble_length)
    while len(buffer) < preamble_length:
        buffer.append(values.popleft())
    while values:
        val = values.popleft()
        if not any(a + b == val for (a, b) in combinations(buffer, 2)):
            print(val)
            break
        buffer.append(val)


if __name__ == "__main__":
    main()
