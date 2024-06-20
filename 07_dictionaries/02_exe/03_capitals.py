countries = input().split(', ')
capitals = input().split(', ')

create_dictionary = dict(zip(countries, capitals))

for k, v in create_dictionary.items():
    print(f'{k} -> {v}')
