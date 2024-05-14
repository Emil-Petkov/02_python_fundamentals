numbers = input().split(' ')

invert_values = []

for num in numbers:
    if num == '':
        break

    invert_values.append(-int(num))

print(invert_values)
