main_list = [int(n) for n in input().split(", ")]
even_list = []

for index, number in enumerate(main_list):
    if number % 2 == 0:
        even_list.append(index)

print(even_list)

# numbers = list(map(int, input().split(', ')))
#
# found_even_indexes = map(lambda x: x if numbers[x] % 2 == 0 else 'no', range(len(numbers)))
#
# even_indexes = list(filter(lambda a: not a == 'no', found_even_indexes))
#
# print(even_indexes)
