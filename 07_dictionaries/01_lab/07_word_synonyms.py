n_lines = int(input())
synonyms = {}

for _ in range(n_lines):
    word = input()
    synonym = input()

    if word not in synonyms.keys():
        synonyms[word] = []
    synonyms[word].append(synonym)

for k, v in synonyms.items():
    print(f'{k} - {", ".join(v)}')
