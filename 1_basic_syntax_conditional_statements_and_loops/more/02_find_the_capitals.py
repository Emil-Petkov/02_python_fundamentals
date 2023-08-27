word = input()

indexes = []

for idx in range(len(word)):
    ch = word[idx]

    if ch.isupper():
        indexes.append(idx)

print(indexes)

# print([ch for ch in word if ch.isupper()])
