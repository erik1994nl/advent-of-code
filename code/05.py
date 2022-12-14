from pathlib import Path

crates_file_path = f"{Path(__file__).parent.parent}\\data\\05_supply_stacks.txt"


def read_crate_input(inp: list):
    stacks_end_idx = inp.index('')
    stacks_inp = inp[:stacks_end_idx]
    moves = inp[stacks_end_idx + 1:]

    # parse stacks

    # parse moves
    def split_moves(m: str):
        s = m.split(' ')
        return int(s[1]), int(s[3]), int(s[5])
    move_details = [
        split_moves(move) for move in moves
    ]

    return [None, move_details]


with open(crates_file_path, 'r') as f:
    crate_input = f.read().splitlines()

    # Part one
    stacks, instructions = read_crate_input(crate_input)
    top_crates = ''

    print(f"Top crates of each stack: {top_crates}")

    # Part two
