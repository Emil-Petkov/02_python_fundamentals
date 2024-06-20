command = input().split(' -> ')
statistic = {}

while not command[0] == 'End':

    company = command[0]
    employee_id = command[1]

    if company not in statistic.keys():
        statistic[company] = []

    if employee_id not in statistic[company]:
        statistic[company].append(employee_id)

    command = input().split(' -> ')

for com in statistic.keys():
    print(f'{com}')

    for id in statistic[com]:
        print(f'-- {id}')
