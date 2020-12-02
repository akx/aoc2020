import re

pw_re = re.compile("^(\d+)-(\d+) (.): (.+)$")

count = 0
for line in open("../inputs/d02-input.txt"):
    pos1, pos2, chr, pw = pw_re.match(line.strip()).groups()
    pos1ok = pw[int(pos1) - 1] == chr
    pos2ok = pw[int(pos2) - 1] == chr
    if (pos1ok or pos2ok) and pos1ok ^ pos2ok:
        count += 1
print(count)
