from dataclasses import dataclass, replace


def read_d08(filename="../inputs/d08-input.txt"):
    ops = []
    with open(filename) as f:
        for l in f:
            op, val = l.split(None, 1)
            val = int(val)
            ops.append((op, val))
    return ops


@dataclass(frozen=True)
class State:
    acc: int
    opc: int

    def jmp(self, val):
        return replace(self, opc=self.opc + val)

    def modify_acc(self, val):
        return replace(self, acc=self.acc + val)


def run_op(state: State, opt):
    op, val = opt
    if op == "nop":
        return state.jmp(1)
    if op == "acc":
        return state.modify_acc(val).jmp(1)
    if op == "jmp":
        return state.jmp(val)
    raise NotImplementedError("...")


def run_until_loop(state, ops):
    opids_seen = set()
    while state.opc < len(ops):
        op = ops[state.opc]
        if state.opc in opids_seen:
            return (state, False)
        opids_seen.add(state.opc)
        state = run_op(state, op)
    return (state, True)
