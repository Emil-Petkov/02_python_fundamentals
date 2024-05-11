budget = int(input())

current_budget = budget

command = input()

while not command == "End":
    if int(command) > current_budget:
        print("You went in overdraft!")
        break

    current_budget -= int(command)
    command = input()

else:
    print("You bought everything needed.")
