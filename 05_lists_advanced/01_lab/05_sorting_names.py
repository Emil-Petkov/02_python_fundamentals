names = input().split(', ')

names.sort()

names.sort(key=len, reverse=True)

print(names)

# names = input().split(', ')
# sorted_alphabetically = sorted(names)
#
# sorted_by_length = sorted(sorted_alphabetically, key=lambda name: -len(name))
#
# print(sorted_by_length)
