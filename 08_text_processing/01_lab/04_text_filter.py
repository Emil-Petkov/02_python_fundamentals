censored_words = input().split(', ')
text = input()

for word in censored_words:
    if word in text:
        text = text.replace(word, len(word) * '*')

print(text)
