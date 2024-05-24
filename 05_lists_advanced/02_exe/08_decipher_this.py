secret_message = input()

words = secret_message.split()

deciphered_message = []

for word in words:
    num = ''
    i = 0
    while i < len(word) and word[i].isdigit():
        num += word[i]
        i += 1

    first_letter = chr(int(num))

    remaining_word = word[i:]

    if len(remaining_word) > 1:
        remaining_word = remaining_word[-1] + remaining_word[1:-1] + remaining_word[0]

    deciphered_word = first_letter + remaining_word

    deciphered_message.append(deciphered_word)

print(' '.join(deciphered_message))
