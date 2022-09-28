first_number = int(input())
second_number = int(input())

print(f'Before:\na = {first_number}\nb = {second_number}')

c = first_number
first_number = second_number
second_number = c

print(f'After:\na = {first_number}\nb = {c}')
