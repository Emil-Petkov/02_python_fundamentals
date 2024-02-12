n_numbers = int(input())

is_special_number = False

for num in range(1, n_numbers + 1):
    sum_of_digits = 0

    for s in str(num):
        sum_of_digits += int(s)

    is_special_number = sum_of_digits in [5, 7, 11]

    if is_special_number:
        print(f'{num} -> True')

    else:
        print(f'{num} -> False')
