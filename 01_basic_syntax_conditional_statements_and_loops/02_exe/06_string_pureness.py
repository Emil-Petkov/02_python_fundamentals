n_lines = int(input())

symbols = [
    ',',
    '.',
    '_',
]

for line in range(n_lines):
    current_text = input()

    if any(symbol in current_text for symbol in symbols):
        print(f'{current_text} is not pure!')

    else:
        print(f'{current_text} is pure.')
