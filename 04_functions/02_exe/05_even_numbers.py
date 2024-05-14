def even_numbers(numbers: list):
    even_numbers = []
    for num in numbers:
        if int(num) % 2 == 0:
            even_numbers.append(int(num))

    return even_numbers


numbers = input().split()
result = even_numbers(numbers)
print(result)
