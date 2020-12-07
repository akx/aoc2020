from d07lib import read_d07

bag_data = read_d07()


def iter_paths(color, path=()):
    has_next = bag_data.get(color, [])
    yield path
    for next_spec in has_next:
        yield from iter_paths(next_spec.color, path=path + (next_spec.color,))


def main():
    roots = set()
    for root_color in bag_data:
        for path in iter_paths(root_color):
            if path and path[-1] == "shiny gold":
                roots.add(root_color)
    print(len(roots))


if __name__ == "__main__":
    main()
