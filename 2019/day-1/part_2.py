total = 0


def find_required_fuel(mass):
    fuel = 0
    while True:
        required_fuel = int(mass) // 3 - 2
        if required_fuel <= 0:
            break
        fuel += required_fuel
        mass = required_fuel
    return fuel


with open('puzzle_input') as f:
    total = 0
    for line in f:
        total += find_required_fuel(int(line.strip()))

print(f'{total}')

