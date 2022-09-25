start_range_of_ascii_table = int(input())
final_range_ascii_table = int(input())

for ascii_range in range(start_range_of_ascii_table, final_range_ascii_table + 1):
    print(chr(ascii_range), end=" ")
