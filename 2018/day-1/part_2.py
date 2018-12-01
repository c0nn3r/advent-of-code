import itertools

PUZZLE_FILEPATH = 'input.txt'

with open(PUZZLE_FILEPATH, 'r') as puzzle_file:
    seen_frequencies = set()
    current_frequency = 0

    for frequency_change in itertools.cycle(puzzle_file):
        current_frequency += int(frequency_change)

        if current_frequency in seen_frequencies:
            print(current_frequency)
            break

        seen_frequencies.add(current_frequency)
