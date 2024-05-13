n_lines = int(input())

positive_number_result = []
negative_number_result = []

for _ in range(n_lines):
    current_number = int(input())

    if current_number > 0:
        positive_number_result.append(current_number)

    else:
        negative_number_result.append(current_number)

print(f'{positive_number_result}\n{negative_number_result}')
print(f'Count of positives: {len(positive_number_result)}')
print(f'Sum of negatives: {sum(negative_number_result)}')
