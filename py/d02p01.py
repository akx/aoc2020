import re

pw_re = re.compile("^(\d+)-(\d+) (.): (.+)$")

count = 0
for line in open("../inputs/d02-input.txt"):
    min, max, chr, pw = pw_re.match(line.strip()).groups()
    if int(min) <= pw.count(chr) <= int(max):
        count += 1
print(count)
