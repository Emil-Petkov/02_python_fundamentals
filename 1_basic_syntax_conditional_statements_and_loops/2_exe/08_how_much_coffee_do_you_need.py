command = input()

number_coffees = 0

events = \
    [
        "coding",
        "CODING",
        "dog",
        "DOG",
        "cat",
        "CAT",
        "movie",
        "MOVIE",
    ]

while not command == "END":

    if command in events:
        if command == command.lower():
            number_coffees += 1

        else:
            number_coffees += 2

    command = input()

if number_coffees > 5:
    print("You need extra sleep")

else:
    print(number_coffees)
