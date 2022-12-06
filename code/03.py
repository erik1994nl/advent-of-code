from pathlib import Path

backpacks_file_path = f"{Path(__file__).parent.parent}\\data\\03_backpacks.txt"

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
       'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
       's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

item_score_lower = {
    letter: abc.index(letter) + 1 for letter in abc
}
item_score_upper = {
    letter.upper(): abc.index(letter) + 27 for letter in abc
}
item_score = {**item_score_lower, **item_score_upper}

with open(backpacks_file_path, 'r') as f:
    backpacks = f.read().splitlines()

    # Part one
    total_score = 0
    for backpack in backpacks:
        split_index = int(len(backpack) / 2)
        compartment_one = set(backpack[:split_index])
        compartment_two = set(backpack[split_index:])
        wrong_item = compartment_one.intersection(compartment_two).pop()
        score = item_score.get(wrong_item, 0)
        total_score += score

    print(f"Sum of wrong item type id's: {total_score}")

    # Part two
    total_score = 0
    for idx in range(0, len(backpacks), 3):
        three_group = backpacks[idx:idx+3]
        common_item = set(three_group[0]).intersection(set(three_group[1])).intersection((set(three_group[2]))).pop()
        score = item_score.get(common_item, 0)
        total_score += score

    print(f"Sum of common three group id's: {total_score}")
