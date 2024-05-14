def smallest_of_three_numbers(f_num: int, s_num: int, t_num: int):
    return min(f_num, s_num, t_num)


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = smallest_of_three_numbers(first_number, second_number, third_number)
print(result)
