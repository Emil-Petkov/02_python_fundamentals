n_letters = int(input())

for i in range(0, n_letters):
    for j in range(0, n_letters):
        for l in range(0, n_letters):
            print(f'{chr(97 + i)}{chr(97 + j)}{chr(97 + l)}')
