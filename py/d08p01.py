def read_d08(filename="../inputs/d08-input.txt"):
    ops = []
    with open(filename) as f:
        for l in f:
            op, val = l.split(None, 1)
            val = int(val)
            ops.append((op, val))
    return ops

def main():
    ops = read_d08()
    opids_seen = set()
    opc = 0
    acc = 0
    while True:
        op, val = ops[opc]
        if opc in opids_seen:
            print(acc)
            break
        opids_seen.add(opc)
        if op == "nop":
            opc += 1
        elif op == "acc":
            acc += val
            opc += 1
        elif op == "jmp":
            opc += val

if __name__ == '__main__':
    main()
