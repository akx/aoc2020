def read_d09(filename="../inputs/d09-input.txt"):
    values = []
    with open(filename) as f:
        for l in f:
            values.append(int(l))
    return values
