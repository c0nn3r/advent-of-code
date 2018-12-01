PUZZLE_FILEPATH = 'input.txt'

with open(PUZZLE_FILEPATH, 'r') as puzzle_file:
    end_frequency = sum(int(frequency_change) for frequency_change in puzzle_file)
    print(end_frequency)
