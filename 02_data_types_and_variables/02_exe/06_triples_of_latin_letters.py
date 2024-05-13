n_letters = int(input())

for i in range(0, n_letters):
    for j in range(0, n_letters):
        for k in range(0, n_letters):
            print(f'{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}')
