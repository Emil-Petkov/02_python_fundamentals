n_iteration = int(input())

for first_loop in range(n_iteration):
    for second_loop in range(n_iteration):
        for third_loop in range(n_iteration):
            print(f'{chr(97 + first_loop)}{chr(97 + second_loop)}{chr(97 + third_loop)}')
