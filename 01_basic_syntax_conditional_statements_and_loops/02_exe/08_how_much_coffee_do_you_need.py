command = input()

count_coffees = 0

events = [
    'coding',
    'dog',
    'cat',
    'movie',
]

while not command == 'END':

    if command.lower() not in events:
        command = input()

        continue

    elif command.isupper():
        count_coffees += 2

    elif command.islower():
        count_coffees += 1

    command = input()

if count_coffees > 5:
    print('You need extra sleep')

else:
    print(count_coffees)
