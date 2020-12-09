from d08lib import read_d08, State, run_until_loop


def main():
    orig_ops = tuple(read_d08())
    *_, cand_ops = run_until_loop(State(opc=0, acc=0), orig_ops)
    for i in cand_ops:
        if orig_ops[i][0] == "acc":
            continue
        ops = list(orig_ops)
        ops[i] = ("jmp" if ops[i][0] == "nop" else "nop", ops[i][1])
        state = State(opc=0, acc=0)
        final_state, finished, _ = run_until_loop(state, ops)
        if finished:
            print(i, final_state)
            break


if __name__ == "__main__":
    main()
