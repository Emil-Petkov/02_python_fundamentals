n_lines = int(input())

total_sum = 0

for line in range(n_lines):
    current_letter = input()

    total_sum += ord(current_letter)

print(f'The sum equals: {total_sum}')
