n_lines = int(input())

total_chars = 0
print_free_chairs = True

for room in range(1, n_lines + 1):
    current_line = input().split()

    n_chars = len(current_line[0])
    needed_chars = int(current_line[1])

    if n_chars >= needed_chars:
        total_chars += abs(n_chars - needed_chars)

    else:
        print(f'{abs(n_chars - needed_chars)} more chairs needed in room {room}')
        print_free_chairs = False

if print_free_chairs:
    print(f'Game On, {total_chars} free chairs left')
