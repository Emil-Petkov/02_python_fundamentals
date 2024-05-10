# print(input()[::-1])

word = input()

reverse_word = ''

for letter in word:
    reverse_word = letter + reverse_word

print(reverse_word)
