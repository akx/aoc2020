import d10lib


def get_result(inputs):
    # via https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gf9b0zz/
    #     https://github.com/bvandewalle/aoc2020/blob/master/10/main.go
    accum = {0: 1}
    for i in inputs:
        accum[i] = accum.get(i - 1, 0) + accum.get(i - 2, 0) + accum.get(i - 3, 0)
    return accum[inputs[-1]]


def main():
    inputs = sorted(d10lib.read_d10())
    inputs.append(inputs[-1] + 3)  # built-in adapter
    assert len(set(inputs)) == len(inputs)  # sanity check for no duplicates
    print(get_result(inputs))


if __name__ == "__main__":
    main()
