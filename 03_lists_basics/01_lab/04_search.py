n_lines = int(input())
search_word = input()

all_text = []
filtered_text = []

for _ in range(n_lines):
    current_text = input()

    all_text.append(current_text)

    if search_word in current_text:
        filtered_text.append(current_text)

print(all_text)
print(filtered_text)
