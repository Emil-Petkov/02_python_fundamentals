def password_validator(guess: str):
    errors = []

    if not 6 <= len(guess) <= 10:
        errors.append('Password must be between 6 and 10 characters')

    digit_count = sum(char.isdigit() for char in guess)
    if digit_count < 2:
        errors.append('Password must have at least 2 digits')

    if not guess.isalnum():
        errors.append('Password must consist only of letters and digits')

    if errors:
        return '\n'.join(errors)

    else:
        return 'Password is valid'


guess_password = input()
result = password_validator(guess_password)
print(result)
