n_numbers = int(input())

for num in range(n_numbers):
    current_number = int(input())

    if current_number % 2 == 0:
        continue

    else:
        print(f'{current_number} is odd!')
        exit()

print('All numbers are even.')
