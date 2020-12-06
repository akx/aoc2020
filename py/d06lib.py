def read_d06():
    SEP = chr(30)
    with open("../inputs/d06-input.txt") as f:
        data = f.read()
        data = data.replace("\n\n", SEP)
    groups = [set(c for c in group if c.isalpha()) for group in data.split(SEP)]
    return groups


if __name__ == "__main__":
    print(read_d06())
