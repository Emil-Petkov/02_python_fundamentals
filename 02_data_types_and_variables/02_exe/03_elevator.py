import math

n_peoples = int(input())
capacity_one_courses = int(input())

total_courses = math.ceil(n_peoples / capacity_one_courses)

print(total_courses)
