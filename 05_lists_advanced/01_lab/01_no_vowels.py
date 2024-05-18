



















text = input()

modified_string = ''

vowels = \
    [
        'a',
        'o',
        'u',
        'e',
        'i',
    ]

for ch in text:
    if ch.lower() in vowels:
        continue

    else:
        modified_string += ch

print(modified_string)
