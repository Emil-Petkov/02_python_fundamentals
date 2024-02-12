command = input()

events = [
    'coding',
    'dog',
    'cat',
    'movie',
]

counter_cup_of_coffee = 0

while not command == 'END':
    current_command = command.lower()

    if current_command in events:
        if command.isupper():
            counter_cup_of_coffee += 2

        else:
            counter_cup_of_coffee += 1

    else:
        command = input()
        continue

    command = input()

if counter_cup_of_coffee > 5:
    print('You need extra sleep')

else:
    print(counter_cup_of_coffee)
