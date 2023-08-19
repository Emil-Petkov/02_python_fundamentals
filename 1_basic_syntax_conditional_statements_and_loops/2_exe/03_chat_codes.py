def message_with_numbers(n_lines):

    for command in range(n_lines):
        current_command = int(input())
        if current_command == 88:
            print("Hello")
        elif current_command == 86:
            print("How are you?")
        elif current_command > 88:
            print("Bye.")
        else:
            print("GREAT!")


n_commands = int(input())
message_with_numbers(n_commands)
