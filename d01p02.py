import itertools

with open("d01-input.txt", "r") as f:
    entries = [int(ent.strip()) for ent in f]
    for a, b, c in itertools.combinations(entries, 3):
        if a + b + c == 2020:
            print(a * b * c)
            break
