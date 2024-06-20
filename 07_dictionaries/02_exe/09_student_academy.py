n_inputs = int(input())
info = {}

for _ in range(n_inputs):
    name = input()
    grade = float(input())

    if name not in info:
        info[name] = []
    info[name].append(grade)

for name, grade in info.items():
    average_grade = sum(info[name]) / len(info[name])

    if average_grade >= 4.50:
        print(f'{name} -> {average_grade:.2f}')
