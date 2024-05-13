n_lines = int(input())

tank_capacity = 255  # liters
total_filled_liters = 0

for _ in range(n_lines):
    current_liters = int(input())

    if total_filled_liters + current_liters > tank_capacity:
        print('Insufficient capacity!')
        continue

    else:
        total_filled_liters += current_liters

print(total_filled_liters)
