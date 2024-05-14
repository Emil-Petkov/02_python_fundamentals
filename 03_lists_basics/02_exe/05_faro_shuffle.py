cards = input().split()
shuffle_count = int(input())

for _ in range(shuffle_count):
    half = len(cards) // 2
    left = cards[:half]
    right = cards[half:]
    shuffled_deck = []

    for i in range(half):
        shuffled_deck.append(left[i])
        shuffled_deck.append(right[i])

    cards = shuffled_deck

print(cards)
