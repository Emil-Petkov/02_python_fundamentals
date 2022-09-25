n_lines = int(input())

capacity_of_tank = 255 #liters
count_empty_space_of_tank = 0

for iteration in range(n_lines):
    current_liters = int(input())
    if capacity_of_tank - current_liters < 0:
        print('Insufficient capacity!')
        continue
    capacity_of_tank -= current_liters
    count_empty_space_of_tank += current_liters
print(count_empty_space_of_tank)


