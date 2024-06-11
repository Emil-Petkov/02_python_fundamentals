



















command = input().split(':')

student_information = {

}

while len(command) > 1:
    name = command[0]
    student_id = command[1]
    course = command[2]

    if course not in student_information:
        student_information[course] = {}

    student_information[course][student_id] = name

    command = input().split(':')

course_name = command[0].replace('_', ' ')

if course_name in student_information:
    for id, name in student_information[course_name].items():
        print(f'{name} - {id}')
