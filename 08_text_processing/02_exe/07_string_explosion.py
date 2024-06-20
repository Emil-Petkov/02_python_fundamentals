text = input()

result = []
strength = 0

i = 0
while i < len(text):
    if text[i] == '>':
        result.append(text[i])
        strength += int(text[i + 1])
    else:
        if strength > 0:
            strength -= 1
        else:
            result.append(text[i])
    i += 1

print("".join(result))
