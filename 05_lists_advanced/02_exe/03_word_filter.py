words = input().split()

even_length_words = [w for w in words if len(w) % 2 == 0]

print('\n'.join(even_length_words))
