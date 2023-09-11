first_str = input()
second_str = input()

last_printed_str = ""

for idx in range(len(first_str)):
    left_part = second_str[:idx + 1]

    right_part = first_str[idx + 1:]

    new_str = left_part + right_part

    if new_str == last_printed_str:
        continue

    print(new_str)

    last_printed_str = new_str
