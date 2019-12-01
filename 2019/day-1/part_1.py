total = 0

with open('puzzle_input') as f:
    for line in f:
        total += int(line.strip()) // 3 - 2

print(f'{total}')
