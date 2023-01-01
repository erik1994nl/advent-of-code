from pathlib import Path
from typing import List

treetop_file = f"{Path(__file__).parent.parent}\\data\\08_treetop_house.txt"


def get_rows_and_cols(tree_grid: List[str]) -> tuple[List[List[str]], List[List[str]]]:
    tree_r = []
    tree_c = [None] * len(tree_grid[0])
    first_row = True

    for t in tree_grid:
        tree_r.append(list(t))
        for tree_idx, tree in enumerate(t):
            if first_row:
                tree_c[tree_idx] = [tree]
            else:
                tree_c[tree_idx].append(tree)
        first_row = False

    return tree_r, tree_c


with open(treetop_file, 'r') as f:
    trees = f.read().splitlines()

    tree_rows, tree_cols = get_rows_and_cols(trees)

    print(f"Part 1: {0}")

    print(f"Part 2: {0}")
