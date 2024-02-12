n_lines = int(input())

for _ in range(n_lines):
    current_text = input()

    if any(char in current_text for char in [',', '.', '_']):
        print(f'{current_text} is not pure!')

    else:
        print(f'{current_text} is pure.')
