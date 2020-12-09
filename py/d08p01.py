from d08lib import read_d08, State, run_until_loop


def main():
    ops = read_d08()
    state = State(opc=0, acc=0)
    state = run_until_loop(state, ops)
    print("final state", state)


if __name__ == "__main__":
    main()
