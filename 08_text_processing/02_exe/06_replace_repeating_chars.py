text = input()
result = []

for i in range(len(text)):
    if i == 0 or text[i] != text[i - 1]:
        result.append(text[i])

print("".join(result))
