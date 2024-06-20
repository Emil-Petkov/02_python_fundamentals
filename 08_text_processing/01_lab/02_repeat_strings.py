data = input().split()
counter = 0
concatenated_string = ''

for word in data:
    for _ in range(len(word)):
        counter += 1

    concatenated_string += (word * counter)

    counter = 0

print(concatenated_string)
