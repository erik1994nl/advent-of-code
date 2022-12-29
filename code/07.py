from pathlib import Path
from collections import defaultdict

full_device_file = f"{Path(__file__).parent.parent}\\data\\07_full_device.txt"


def get_sizes(lines):
    # Remove ls commands
    lines = [entry for entry in lines if entry != "$ ls"]
    filepath = []
    s = defaultdict(int)

    for entry in lines:
        if entry == "$ cd /":
            filepath.clear()
            filepath.append("/")
        elif entry == "$ cd ..":
            filepath.pop()
        elif entry.startswith("$ cd"):
            d = entry.split()[-1]
            filepath.append(d)
        else:
            # We have a listing of a file. Add the size to the current dir and all of its parent dirs.
            filesize = entry.split()[0]
            if filesize.isdigit():
                filesize = int(filesize)
                # Iterate through every dir in the full path to the file
                for i in range(len(filepath)):
                    d = '/'.join(filepath[:i+1]).replace("//", "/")
                    s[d] += filesize
    return s


with open(full_device_file, 'r') as f:
    device = f.read().splitlines()

    sizes = get_sizes(device)
    dirs_below_threshold = {directory: size for (directory, size) in sizes.items() if size <= 100000}
    print(f"Part 1: {sum(dirs_below_threshold.values())}")

    size_available = 70_000_000 - sizes['/']
    size_needed = 30_000_000 - size_available
    sorted_sizes = sorted([
        s for k, s in sizes.items()
    ])
    size_to_remove = None
    for candidate_size in sorted_sizes:
        if candidate_size > size_needed:
            size_to_remove = candidate_size
            break

    print(f"Part 2: {size_to_remove}")
