command = input()

while True:
    if command == "End":
        break
    elif command == "SoftUni":
        command = input()
        continue
    else:
        print("".join([ch * 2 for ch in command]))
        command = input()
