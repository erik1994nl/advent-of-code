from pathlib import Path
from collections import deque

input_signal_file = f"{Path(__file__).parent.parent}\\data\\06_tuning_trouble.txt"


def get_start_marker(cache_size: int) -> int:
    cache = deque(input_signal[:cache_size], maxlen=cache_size)
    sop = -1
    for idx, input_char in enumerate(input_signal[cache_size:], cache_size):
        if len(set(cache)) == cache_size:
            sop = idx
            break
        else:
            cache.append(input_char)
    return sop


with open(input_signal_file, 'r') as f:
    input_signal = f.read()

    # Part one
    start_of_packet = get_start_marker(4)
    print(f"Start of packet index: {start_of_packet}")

    # Part two
    start_of_message = get_start_marker(14)
    print(f"Start of packet index: {start_of_message}")
