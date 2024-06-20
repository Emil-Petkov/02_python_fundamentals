person = input().split('-')
phonebook = {}

while not len(person) == 1:
    name, phone = person
    phonebook[name] = phone
    person = input().split('-')

n_names = int(person[0])

for _ in range(n_names):
    current_name = input()

    if current_name in phonebook.keys():
        print(f'{current_name} -> {phonebook[current_name]}')
    else:
        print(f'Contact {current_name} does not exist.')
