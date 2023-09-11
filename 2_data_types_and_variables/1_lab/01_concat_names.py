def full_name(f_name, l_name, delimiter):
    return f"{f_name} {delimiter} {l_name}"


first_name, last_name, delimiter = input(), input(), input()

print(full_name(first_name, last_name, delimiter))
