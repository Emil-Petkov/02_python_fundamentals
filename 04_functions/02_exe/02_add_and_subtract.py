def add(first_number: int, second_number: int):
    return first_number + second_number


def subtract(add_result: int, third_number):
    return add_result - third_number


first_number = int(input())
second_number = int(input())
third_number = int(input())

final_result = subtract(add(first_number, second_number), third_number)
print(final_result)
