command = input()

while not command == 'end':
    reverse_word = command[::-1]

    print(f'{command} = {reverse_word}')

    command = input()
