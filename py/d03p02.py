from functools import reduce
from operator import mul


def main():
    max_x, max_y, trees = read()
    counts = []
    for dx, dy in (1, 1), (3, 1), (5, 1), (7, 1), (1, 2):
        counts.append(count_trees(max_x, max_y, trees, dx, dy))
    mul_count = reduce(mul, counts)
    print(mul_count)


def count_trees(max_x, max_y, trees, dx, dy):
    x, y = 0, 0
    count = 0
    while y <= max_y:
        if (x % max_x, y) in trees:
            count += 1
        x += dx
        y += dy
    return count


def read():
    trees = set()
    for y, line in enumerate(open("../inputs/d03-input.txt")):
        for x, c in enumerate(line):
            if c == "#":
                trees.add((x, y))
    return x, y, trees


if __name__ == '__main__':
    main()
