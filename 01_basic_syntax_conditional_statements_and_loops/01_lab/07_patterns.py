n_stars = int(input())

for star in range(1, n_stars + 1):
    print('*' * star)

for rev_star in range(n_stars - 1, 0, -1):
    print('*' * rev_star)
