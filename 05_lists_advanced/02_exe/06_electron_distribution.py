electrons = int(input())

n = 1
distribution = []

while electrons > 0:
    max_electrons_in_shell = 2 * (n ** 2)
    if electrons >= max_electrons_in_shell:
        distribution.append(max_electrons_in_shell)
        electrons -= max_electrons_in_shell
    else:
        distribution.append(electrons)
        electrons = 0
    n += 1

print(distribution)
