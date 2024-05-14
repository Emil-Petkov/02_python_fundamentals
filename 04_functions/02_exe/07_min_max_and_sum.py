import sys


def min_max_and_sum(numbers: list):
    max_number = -sys.maxsize
    min_number = sys.maxsize
    sum_of_numbers = 0

    convert_to_integers = map(int, numbers)

    for num in convert_to_integers:
        if num > max_number:
            max_number = num

        if num < min_number:
            min_number = num

        sum_of_numbers += num

    return max_number, min_number, sum_of_numbers


numbers = input().split()
max_number, min_number, sum_of_numbers = min_max_and_sum(numbers)
print(f'The minimum number is {min_number}')
print(f'The maximum number is {max_number}')
print(f'The sum number is: {sum_of_numbers}')
