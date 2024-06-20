command = input()
count_materials = {}

while not command == 'stop'.lower():
    quantity = int(input())

    if command not in count_materials:
        count_materials[command] = 0
    count_materials[command] += quantity

    command = input()

for k, v in count_materials.items():
    print(f'{k} -> {v}')
