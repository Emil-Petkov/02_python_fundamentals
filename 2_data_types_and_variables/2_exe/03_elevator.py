from math import ceil

n_peoples = int(input())
elevator_capacity = int(input())

calculate = ceil(n_peoples / elevator_capacity)

print(calculate)
