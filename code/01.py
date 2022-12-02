from pathlib import Path

calories_file_path = f"{Path(__file__).parent.parent}\\data\\01_calories.txt"

with open(calories_file_path, 'r') as f:
    calories = f.read().splitlines()

    total_calories = []
    last_space = 0
    while True:
        try:
            new_space = calories.index('', last_space + 1)
        except ValueError as out_of_bounds:
            # You have reached the last elf
            break
        total_calories.append(sum([int(cal) for cal in calories[last_space:new_space]]))
        last_space = new_space + 1

    total_calories.sort()
    print(f"Max calories: {total_calories[-1:]}")
    print(f"Sum of top 3: {sum(total_calories[-3:])}")