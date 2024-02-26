n_lines = int(input())

water_in_tank = 0  # liters

for w in range(n_lines):
    current_liters = int(input())

    if water_in_tank + current_liters <= 255:
        water_in_tank += current_liters
        continue

    print('Insufficient capacity!')

print(water_in_tank)
