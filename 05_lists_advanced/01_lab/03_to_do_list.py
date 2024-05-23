command = input()

to_do_list = ['' for _ in range(11)]

while not command == 'End':
    explode = command.split('-')

    number = int(explode[0])
    event = explode[1]

    to_do_list[number] = event

    command = input()

result = [i for i in to_do_list if i.strip()]

print(result)
