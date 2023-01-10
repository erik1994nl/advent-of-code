from pathlib import Path
from typing import List

treetop_file = f"{Path(__file__).parent.parent}\\data\\08_treetop_house.txt"


def get_rows_and_cols(tree_grid: List[str]):
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


def is_visible(tree_line: List[str], tree_idx: int) -> bool:
    if tree_idx == 0 or tree_idx == len(tree_line) - 1:
        return True
    perspective_one = tree_line[tree_idx] > max(tree_line[:tree_idx])
    perspective_two = tree_line[tree_idx] > max(tree_line[tree_idx+1:])
    return perspective_one or perspective_two


def get_visibility_grid(rows: List[List[str]], cols: List[List[str]]):
    visibility = []
    for x in range(len(cols)):
        visibility.append([])
        for y in range(len(rows)):
            visibility[x].append(is_visible(rows[y], x) or is_visible(cols[x], y))

    return visibility


with open(treetop_file, 'r') as f:
    trees = f.read().splitlines()

    tree_rows, tree_cols = get_rows_and_cols(trees)

    visibility_grid = get_visibility_grid(tree_rows, tree_cols)

    print(f"Part 1: {0}")

    print(f"Part 2: {0}")
