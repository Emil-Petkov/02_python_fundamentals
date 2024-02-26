n_lines = int(input())

sum_of_chars = 0

for ch in range(n_lines):
    current_char = input()
    sum_of_chars += ord(current_char)

print(f'The sum equals: {sum_of_chars}')
