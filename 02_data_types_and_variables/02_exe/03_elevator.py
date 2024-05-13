import math

n_peoples = int(input())
capacity = int(input())

courses_of_the_elevator = math.ceil(n_peoples / capacity)

print(courses_of_the_elevator)
