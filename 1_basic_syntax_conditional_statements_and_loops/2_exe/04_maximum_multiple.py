def maximum_multiple(divisor, boundary):
    how_many_times = boundary // divisor

    return how_many_times * divisor


divisor = int(input())
boundary = int(input())
print(maximum_multiple(divisor, boundary))
