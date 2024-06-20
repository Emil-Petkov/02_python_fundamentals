data = input().split()
str1, str2 = data[0], data[1]
total_sum = 0

min_len = min(len(str1), len(str2))

for i in range(min_len):
    total_sum += ord(str1[i]) * ord(str2[i])

if len(str1) > len(str2):
    for i in range(min_len, len(str1)):
        total_sum += ord(str1[i])

elif len(str2) > len(str1):
    for i in range(min_len, len(str2)):
        total_sum += ord(str2[i])

print(total_sum)
