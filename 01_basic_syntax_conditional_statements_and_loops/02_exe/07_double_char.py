command = input()

while not command == "End":
    current_command = command

    if current_command == 'SoftUni':
        command = input()
        continue

    for char in current_command:
        print(char * 2, end='')

    print()
    command = input()
