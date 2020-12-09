from d08lib import read_d08, State, run_op


def run_until_loop(state, ops):
    opids_seen = set()
    while state.opc < len(ops):
        op = ops[state.opc]
        if state.opc in opids_seen:
            break
        opids_seen.add(state.opc)
        state = run_op(state, op)
    return state


def main():
    ops = read_d08()
    state = State(opc=0, acc=0)
    state = run_until_loop(state, ops)
    print("final state", state)


if __name__ == "__main__":
    main()
