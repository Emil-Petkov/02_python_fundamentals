n_numbers = int(input())

positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []

for _ in range(n_numbers):
    current_number = int(input())

    if current_number >= 0:
        positive_numbers.append(current_number)

    if current_number < 0:
        negative_numbers.append(current_number)

    if current_number % 2 == 0:
        even_numbers.append(current_number)

    else:
        odd_numbers.append(current_number)

operations = {
    'positive': positive_numbers,
    'negative': negative_numbers,
    'even': even_numbers,
    'odd': odd_numbers,
}

command = input()

if command in operations:
    print(operations[command])
