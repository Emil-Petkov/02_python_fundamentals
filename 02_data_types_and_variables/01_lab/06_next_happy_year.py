current_year = int(input())

current_year += 1

while True:
    next_happy_year = set(str(current_year))

    if len(next_happy_year) == len(str(current_year)):
        print(current_year)
        break

    current_year += 1
