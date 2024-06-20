random_string = input()

digits = ''.join([i for i in random_string if i.isdigit()])
letters = ''.join([i for i in random_string if i.isalpha()])
symbols = ''.join([i for i in random_string if not (i.isdigit() or i.isalpha())])

print(f'{digits}\n{letters}\n{symbols}')
