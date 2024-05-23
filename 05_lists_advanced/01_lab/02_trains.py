number_of_wagons = int(input())

train = [0] * number_of_wagons

command = input()

while not command == 'End':
    current_command = command.split(' ')

    if current_command[0] == 'add':
        passengers = int(current_command[1])
        train[-1] += passengers

    elif current_command[0] == 'insert':
        index = int(current_command[1])
        passengers = int(current_command[2])

        if 0 <= index < number_of_wagons:
            train[index] += passengers

    elif current_command[0] == 'leave':
        index = int(current_command[1])
        passengers = int(current_command[2])

        if 0 <= index < number_of_wagons:
            train[index] -= passengers

    command = input()

print(train)
