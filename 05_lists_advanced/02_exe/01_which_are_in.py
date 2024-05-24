first_line_words = input().split(', ')
second_line_words = input().split(', ')

found_words = []

for first_string in first_line_words:
    for second_string in second_line_words:
        if first_string in second_string:
            found_words.append(first_string)
            break

print(found_words)
