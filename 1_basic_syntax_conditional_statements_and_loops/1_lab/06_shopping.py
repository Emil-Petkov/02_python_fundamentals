budget = int(input())
command = input()
current_budget = budget

while command != 'End':
    product_price = int(command)
    current_budget -= product_price

    if current_budget < 0:
        print('You went in overdraft!')
        break
    command = input()
else:
    print('You bought everything needed.')
