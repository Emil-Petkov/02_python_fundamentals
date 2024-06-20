command = input().split(' : ')

info = {}

while not command[0] == 'end':
    course = command[0]
    name = command[1]

    if course not in info.keys():
        info[course] = []
    info[course].append(name)

    command = input().split(' : ')

for course, students in info.items():
    print(f'{course}: {len(students)}')

    for student in students:
        print(f'-- {student}')
