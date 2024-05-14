def calculations(oper: str, f_num: int, s_num: int):
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y,
    }

    if oper in operations:
        return operations[oper](f_num, s_num)


operation = input()
first_number = int(input())
second_number = int(input())

result = calculations(operation, first_number, second_number)
print(f'{result:.0f}')
