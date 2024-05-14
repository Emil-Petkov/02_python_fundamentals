def sort(numbers: list):
    return sorted(map(int, numbers))


numbers = input().split()
result = sort(numbers)
print(result)
