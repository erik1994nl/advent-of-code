from pathlib import Path

rope_bridge_file = f"{Path(__file__).parent.parent}\\data\\09_rope_bridge.txt"

with open(rope_bridge_file, 'r') as f:
    bridge = f.read().splitlines()

    tail_pos = (0, 0)
    head_pos = (0, 0)

    for direction, _, *steps in bridge:
        steps = int(''.join(steps))
        print(f"d: {direction} - s: {steps}")

    print(f"Part 1: {0}")

    print(f"Part 2: {0}")
