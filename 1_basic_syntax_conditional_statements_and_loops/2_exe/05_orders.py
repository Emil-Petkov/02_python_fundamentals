n_orders = int(input())

total = 0

for i in range(1, n_orders + 1):
    capsule_price = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())

    if capsule_price < 0.01 or capsule_price > 100.00:
        continue
    elif needed_capsules_per_day < 1 or needed_capsules_per_day > 2000:
        continue
    elif days < 1 or days > 31:
        continue

    profit = (capsule_price * needed_capsules_per_day) * days
    total += profit

    print(f'The price for the coffee is: ${profit:.2f}')

print(f'Total: ${total:.2f}')
