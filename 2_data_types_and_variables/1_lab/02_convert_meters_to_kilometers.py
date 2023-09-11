def meters_to_km(meters):
    return f"{meters / 1000:.2f}"


meters = int(input())

print(meters_to_km(meters))
