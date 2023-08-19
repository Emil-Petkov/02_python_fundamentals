def check_for_even_number(n_numbers):
    for num in range(n_numbers):
        current_number = int(input())
        if current_number % 2 == 0:
            continue
        else:
            return f"{current_number} is odd!"

    return "All numbers are even."


n_numbers = int(input())
print(check_for_even_number(n_numbers))
