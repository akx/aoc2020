from typing import List

import d10lib


def walk_combos(adapters: List[int], start_index: int, cache: dict):
    if start_index in cache:
        return cache[start_index]
    n = 0
    for next_index in range(start_index + 1, len(adapters)):
        if adapters[next_index] - adapters[start_index] <= 3:
            n += walk_combos(adapters, next_index, cache)
        else:
            break
    n = n or 1
    cache[start_index] = n
    return n


def main():
    inputs = sorted(d10lib.read_d10())
    inputs.insert(0, 0)  # virtual zero
    inputs.append(inputs[-1] + 3)  # built-in adapter
    assert len(set(inputs)) == len(inputs)  # sanity check for no duplicates
    print(walk_combos(inputs, 0, {}))


if __name__ == "__main__":
    main()
