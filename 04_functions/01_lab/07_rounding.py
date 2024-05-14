def rounding(numbers: list):
    lst_of_rounding_numbers = []

    for num in numbers:
        lst_of_rounding_numbers.append(round(float(num)))

    return lst_of_rounding_numbers


numbers = input().split(' ')
result = rounding(numbers)
print(result)
