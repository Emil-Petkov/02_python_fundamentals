n_lines = int(input())

special_numbers = [5, 7, 11]

for line in range(1, n_lines + 1):
    current_number = str(line)
    sum_numbers = 0

    for num in current_number:
        sum_numbers += int(num)

    if sum_numbers in special_numbers:
        print(f'{current_number} -> True')

    else:
        print(f'{current_number} -> False')
