from d09lib import read_d09, get_weakness


def main():
    secret = get_weakness()
    values = list(read_d09())
    for a in range(len(values)):
        for b in range(a, len(values)):
            val_range = values[a:b]
            if sum(val_range) == secret:
                x = min(val_range) + max(val_range)
                print(x)
                return


if __name__ == "__main__":
    main()
