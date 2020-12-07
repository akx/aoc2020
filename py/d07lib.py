import re
from dataclasses import dataclass

line_re = re.compile(r"^(?P<source>.+?) contain (?P<dest>.+?)\.$")
bag_re = re.compile(r"(?P<count>\d+)?\s*(?P<color>[^,]+) bag[s]?")


@dataclass
class BagSpec:
    count: int
    color: str


def to_bagspecs(s):
    for atom in re.split(",\s*", s):
        bag = bag_re.match(atom)
        if not bag:
            print(atom)
            raise NotImplementedError("...")
        if bag.group(0) == "no other bags":
            continue
        yield BagSpec(count=int(bag.group("count") or 1), color=bag.group("color"))


def read_d07(filename="../inputs/d07-input.txt"):
    bag_specs = {}
    with open(filename) as f:
        for line in f:
            m = line_re.match(line)
            assert m
            src, dest = m.groups()
            src_bag = next(to_bagspecs(src)).color
            dest_bags = list(to_bagspecs(dest))
            assert src_bag not in bag_specs
            bag_specs[src_bag] = dest_bags
    return bag_specs


if __name__ == "__main__":
    x = read_d07()
    print(x)
