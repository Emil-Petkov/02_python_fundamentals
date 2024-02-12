command = input()

while not command == 'Voldemort':

    current_name = command

    if current_name == 'Welcome!':
        print('Welcome to Hogwarts.')
        exit()

    elif len(current_name) < 5:
        print(f'{current_name} goes to Gryffindor.')

    elif len(current_name) == 5:
        print(f'{current_name} goes to Slytherin.')

    elif len(current_name) == 6:
        print(f'{current_name} goes to Ravenclaw.')

    else:
        print(f'{current_name} goes to Hufflepuff.')

    command = input()

print('You must not speak of that name!')
