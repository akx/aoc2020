from d06lib import read_d06

groups = read_d06()
print(sum(len(set("".join(g))) for g in groups))
