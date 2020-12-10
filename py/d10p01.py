from d10lib import read_d10


def main():
    inputs = sorted(read_d10())
    deltas = []
    last = 0
    while inputs:
        curr = inputs.pop(0)
        deltas.append(curr - last)
        last = curr
    d1 = deltas.count(1)
    d3 = deltas.count(3) + 1  # lol, fudge factor
    print(d1, d3, d1 * d3)


if __name__ == "__main__":
    main()
