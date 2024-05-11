def find_largest_divisible(divisor: int, bound: int):
    for n in range(bound, 0, -1):
        if n % divisor == 0:
            return n


divisor = int(input())
bound = int(input())

result = find_largest_divisible(divisor, bound)
print(result)
