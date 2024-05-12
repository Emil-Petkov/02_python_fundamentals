current_year = int(input())

while True:
    current_year += 1
    next_happy_year = set(str(current_year))

    if len(str(current_year)) == len(next_happy_year):
        print(current_year)
        break
