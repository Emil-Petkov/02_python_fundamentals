def absolute_values(numbers: list) -> list:
    result = []

    for num in numbers:
        result.append(abs(float(num)))

    return result


numbers = input().split(' ')

print(absolute_values(numbers))
