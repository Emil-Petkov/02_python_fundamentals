first_index = int(input())
second_index = int(input())

result = []

for ch in range(first_index, second_index + 1):
    result.append(chr(ch))

print(' '.join(result))
