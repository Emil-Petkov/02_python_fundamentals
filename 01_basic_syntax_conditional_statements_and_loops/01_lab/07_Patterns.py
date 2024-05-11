n_stars = int(input())

for i in range(n_stars + 1):
    print('*' * i)

for j in range(n_stars - 1, -1, -1):
    print('*' * j)
