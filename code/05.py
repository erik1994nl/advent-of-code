from pathlib import Path

crates_file_path = f"{Path(__file__).parent.parent}\\data\\05_supply_stacks.txt"


def read_crate_input(inp: list):
    stacks_end_idx = inp.index('')
    stacks_inp = inp[:stacks_end_idx]
    moves = inp[stacks_end_idx + 1:]

    # parse stacks
    first = True
    stack_dict = {}
    for stack_row in reversed(stacks_inp):
        if first:
            first = False
            stack_dict = {int(el): [] for el in stack_row[1::4]}
            continue
        for idx, crate in enumerate(stack_row[1::4]):
            if crate != ' ':
                stack_dict[idx + 1].append(crate)

    # parse moves
    def split_moves(m: str):
        s = m.split(' ')
        return int(s[1]), int(s[3]), int(s[5])
    move_details = [
        split_moves(move) for move in moves
    ]

    return [stack_dict, move_details]


def perform_instructions(_stacks: dict[int, list[str]], _instr: list[tuple[int, int, int]]) -> None:
    for amt, _from, _to in _instr:
        for mov in range(amt):
            c = _stacks.get(_from).pop()
            _stacks.get(_to).append(c)
    return None


def perform_instructions_part_2(_stacks: dict[int, list[str]], _instr: list[tuple[int, int, int]]) -> None:
    for amt, _from, _to in _instr:
        crates_to_move = _stacks.get(_from)[-amt:]
        # Remove from old stack
        _stacks[_from] = _stacks.get(_from)[:-amt]
        # Add to new stack
        _stacks.get(_to).extend(crates_to_move)

    return None


with open(crates_file_path, 'r') as f:
    crate_input = f.read().splitlines()

    # Part one
    stacks, instructions = read_crate_input(crate_input)
    perform_instructions(stacks, instructions)
    top_crates = ''.join([stack_crates[-1] for stack_crates in stacks.values()])

    print(f"Top crates of each stack: {top_crates}")

    # Part two
    stacks, instructions = read_crate_input(crate_input)
    perform_instructions_part_2(stacks, instructions)
    top_crates = ''.join([stack_crates[-1] for stack_crates in stacks.values()])

    print(f"Top crates of each stack part 2: {top_crates}")
