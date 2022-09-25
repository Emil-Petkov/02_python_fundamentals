special_number = int(input())


for number in range(1, special_number + 1):
    sum = 0
    digits = number

    while digits > 0:
        sum += digits % 10
        digits = int(digits / 10)

    if sum == 5 or sum == 7 or sum == 11:
        print(f'{number} -> True')
    else:
        print(f'{number} -> False')
