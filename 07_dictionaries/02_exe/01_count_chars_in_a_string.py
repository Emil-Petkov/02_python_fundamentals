text = input().replace(' ', '')
count_letter = {}

for l in text:
    if l not in count_letter.keys():
        count_letter[l] = 0
    count_letter[l] += 1

for k, v in count_letter.items():
    print(f'{k} -> {v}')
