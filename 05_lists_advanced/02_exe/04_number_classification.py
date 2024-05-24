numbers = [int(num) for num in input().split(', ')]

positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []

for num in numbers:
    if num >= 0:
        positive_numbers.append(num)

    if num < 0:
        negative_numbers.append(num)

    if num % 2 == 0:
        even_numbers.append(num)

    else:
        odd_numbers.append(num)

print(f'Positive: {", ".join(map(str, positive_numbers))}')
print(f'Negative: {", ".join(map(str, negative_numbers))}')
print(f'Even: {", ".join(map(str, even_numbers))}')
print(f'Odd: {", ".join(map(str, odd_numbers))}')
