


command = input()

while not command == 'End':
    if command == 'SoftUni':

        command = input()
        continue

    else:
        for ch in command:
            print(ch * 2, end='')

        print()

    command = input()
