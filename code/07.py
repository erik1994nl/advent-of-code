from pathlib import Path

full_device_file = f"{Path(__file__).parent.parent}\\data\\07_full_device.txt"

with open(full_device_file, 'r') as f:
    device = f.read().splitlines()

    # Part one
    print(f"Answer part 1")

    # Part two
    print(f"Answer part 2")
