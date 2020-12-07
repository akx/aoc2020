from typing import Iterable

from d07lib import read_d07, BagSpec

bag_data = read_d07()


def recurse_bags(next: Iterable[BagSpec]):
    for bag_spec in next:
        for x in range(bag_spec.count):
            yield bag_spec.color
            yield from recurse_bags(bag_data.get(bag_spec.color, []))


def main():
    total = 0
    for bag in recurse_bags(bag_data["shiny gold"]):
        total += 1
    print(total)


if __name__ == "__main__":
    main()
