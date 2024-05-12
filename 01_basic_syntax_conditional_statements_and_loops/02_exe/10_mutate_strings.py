initial_string = input()
target_string = input()

if len(initial_string) != len(target_string):
    print("Strings must be of equal length.")

else:
    seen_strings = set()
    current_string = initial_string

    for i in range(len(initial_string)):
        if current_string[i] != target_string[i]:
            current_string = current_string[:i] + target_string[i] + current_string[i + 1:]

            if current_string not in seen_strings:
                seen_strings.add(current_string)

                print(current_string)
