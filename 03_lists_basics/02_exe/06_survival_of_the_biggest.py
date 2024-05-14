numbers = list(map(int, input().split()))
count_to_remove = int(input())

for _ in range(count_to_remove):
    smallest = min(numbers)
    numbers.remove(smallest)

print(', '.join(map(str, numbers)))
