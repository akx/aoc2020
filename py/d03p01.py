trees = set()
for y, line in enumerate(open("../inputs/d03-input.txt")):
    for x, c in enumerate(line):
        if c == "#":
            trees.add((x, y))
max_y = y
max_x = x
x, y = 0, 0
dx, dy = 3, 1
count = 0
while y <= max_y:
    if (x % max_x, y) in trees:
        count += 1
    x += dx
    y += dy
print(count)
