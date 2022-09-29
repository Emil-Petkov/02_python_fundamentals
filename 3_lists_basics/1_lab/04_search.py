numbers_of_lines = int(input())
word = input()
text = []

for i in range(numbers_of_lines):
    current_text = input()
    text.append(current_text)
print(text)

for i in range(len(text) - 1, -1, -1):
    elements = text[i]
    if word not in elements:
        text.remove(elements)
print(text)
