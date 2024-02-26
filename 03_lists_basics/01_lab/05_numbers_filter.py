n_lines = int(input())

mapper = {
    'positive': [],
    'negative': [],
    'even': [],
    'odd': [],
}

for _ in range(n_lines):
    command = input()

    while command not in ['positive', 'negative', 'even', 'odd']:
        if int(command) >= 0:
            mapper['positive'].append(int(command))

        if int(command) < 0:
            mapper['negative'].append(int(command))

        if int(command) % 2 == 0:
            mapper['even'].append(int(command))

        if not int(command) % 2 == 0:
            mapper['odd'].append(int(command))

        command = input()

    print(mapper[command])
    break
