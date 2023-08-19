budget = int(input())
command = int(input())

current_budget = budget

while not command == "End":
    current_budget -= int(command)

    if current_budget < 0:
        print("You went in overdraft!")
        break

    command = input()

else:
    print("You bought everything needed.")
