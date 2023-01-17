from pathlib import Path
from typing import List
import numpy as np

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
            v_1 = is_visible(rows[y], x)
            v_2 = is_visible(cols[x], y)
            visibility[x].append(v_1 or v_2)

    return visibility


def get_scenic_score(row: List[str], col: List[str], x: int, y: int) -> int:
    tree_height = int(col[y])
    left_score = 0
    right_score = 0
    up_score = 0
    down_score = 0


    offset = 1
    while True:
        if x - offset < 0:
            break
        left_score += 1
        if int(row[x - offset]) >= tree_height:
            break
        offset += 1

    offset = 1
    while True:
        if x + offset > (len(row) - 1):
            break
        right_score += 1
        if int(row[x + offset]) >= tree_height:
            break
        offset += 1

    offset = 1
    while True:
        if y - offset < 0:
            break
        up_score += 1
        if int(col[y - offset]) >= tree_height:
            break
        offset += 1

    offset = 1
    while True:
        if y + offset > (len(col) - 1):
            break
        down_score += 1
        if int(col[y + offset]) >= tree_height:
            break
        offset += 1

    scenic_score = left_score * right_score * up_score * down_score
    return scenic_score


def get_max_scenic_score(rows: List[List[str]], cols: List[List[str]]) -> int:
    max_scenic_score = 0
    for x in range(len(cols)):
        for y in range(len(rows)):
            scenic_score = get_scenic_score(rows[y], cols[x], x, y)
            max_scenic_score = max(max_scenic_score, scenic_score)
    return max_scenic_score


with open(treetop_file, 'r') as f:
    trees = f.read().splitlines()

    tree_rows, tree_cols = get_rows_and_cols(trees)

    visibility_grid = get_visibility_grid(tree_rows, tree_cols)

    num_visible = sum(np.sum(visibility_grid, axis=0))
    print(f"Part 1: {num_visible}")

    max_score = get_max_scenic_score(tree_rows, tree_cols)
    print(f"Part 2: {max_score}")
