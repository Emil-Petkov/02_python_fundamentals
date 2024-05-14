numbers_str = input()
beggars_count = int(input())

numbers_list = [int(x) for x in numbers_str.split(", ")]

beggars_sums = [0] * beggars_count

for i in range(len(numbers_list)):
    beggars_sums[i % beggars_count] += numbers_list[i]

print(beggars_sums)
