data = input().split(', ')

correct_usernames = []

for word in data:
    if 3 <= len(word) <= 16:
        if all(char.isalnum() or char in ['-', '_'] for char in word):
            if word[0].isalnum() and word[-1].isalnum():
                correct_usernames.append(word)

print("\n".join(correct_usernames))
