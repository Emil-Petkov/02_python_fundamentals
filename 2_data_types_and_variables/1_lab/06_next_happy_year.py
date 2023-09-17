current_year = int(input())

while True:
    next_happy_year = set()

    for ch in str(current_year):
        next_happy_year.add(ch)

    if len(next_happy_year) == 4:
        print(current_year)
        break
    else:
        current_year += 1
