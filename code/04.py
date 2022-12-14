from pathlib import Path

sections_file_path = f"{Path(__file__).parent.parent}\\data\\04_camp_cleanup.txt"

with open(sections_file_path, 'r') as f:
    sections = f.read().splitlines()

    # Part one
    overlaps = 0
    for full_section in sections:
        (elf_one_start, elf_one_end), (elf_two_start, elf_two_end) = [
            el.split('-') for el in full_section.split(',')
        ]

        if (
                (int(elf_one_start) <= int(elf_two_start) and int(elf_one_end) >= int(elf_two_end))
                or (int(elf_two_start) <= int(elf_one_start) and int(elf_two_end) >= int(elf_one_end))
        ):
            overlaps += 1

    print(f"Number of fully overlapping assignment pairs: {overlaps}")

    # Part two
    overlaps = 0
    for full_section in sections:
        (elf_one_start, elf_one_end), (elf_two_start, elf_two_end) = [
            el.split('-') for el in full_section.split(',')
        ]

        if (
                (int(elf_one_start) <= int(elf_two_start) <= int(elf_one_end))
            or (int(elf_one_start) <= int(elf_two_end) <= int(elf_one_end))
            or (int(elf_one_start) > int(elf_two_start) and int(elf_one_end) < int(elf_two_end))
        ):
            overlaps += 1

    print(f"Number of fully or partly overlapping assignment pairs: {overlaps}")
