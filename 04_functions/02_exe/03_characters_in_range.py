def characters_in_range(start_character: str, end_character: str):
    list_of_characters = []

    for ch in range(ord(start_character) + 1, ord(end_character)):
        list_of_characters.append(chr(ch))

    return list_of_characters


start_character = input()
end_character = input()
result = characters_in_range(start_character, end_character)
print(' '.join(result))
