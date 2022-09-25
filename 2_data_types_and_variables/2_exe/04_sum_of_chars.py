n_characters = int(input())

total_sum = 0

for i in range(n_characters):
    current_character = input()
    total_sum += ord(current_character)

print(f'The sum equals: {total_sum}')
