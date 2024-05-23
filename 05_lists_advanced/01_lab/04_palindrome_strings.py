


















words = input().split()
search_palindrome = input()

all_palindromes = []

counter = 0

for word in words:
    if word == word[::-1]:
        all_palindromes.append(word)

        if word == search_palindrome:
            counter += 1

print(f'{all_palindromes}\nFound palindrome {counter} times')
