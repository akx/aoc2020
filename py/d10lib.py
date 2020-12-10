example1 = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]
example2 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]


def read_d10(filename="../inputs/d10-input.txt"):
    values = []
    with open(filename) as f:
        for l in f:
            values.append(int(l))
    return values
