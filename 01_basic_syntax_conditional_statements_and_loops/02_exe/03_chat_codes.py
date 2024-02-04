n_lines = int(input())

for _ in range(n_lines):
    current_number = int(input())

    if current_number == 88:
        print('Hello')

    elif current_number == 86:
        print('How are you?')

    elif current_number > 88:
        print('Bye.')

    else:
        print('GREAT!')
