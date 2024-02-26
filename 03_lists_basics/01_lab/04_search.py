n_lines = int(input())
key_word = input()

all_sentences = []
filter_sentences = []

for _ in range(n_lines):
    current_line = input()
    all_sentences.append(current_line)

    if key_word in current_line:
        filter_sentences.append(current_line)

print(all_sentences)
print(filter_sentences)
