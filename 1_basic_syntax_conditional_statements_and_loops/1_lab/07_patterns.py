n_lines = int(input())

for i in range(1, n_lines + 1):
    print(i * "*")

for j in range(n_lines - 1, -1, -1):
    print(j * "*")
