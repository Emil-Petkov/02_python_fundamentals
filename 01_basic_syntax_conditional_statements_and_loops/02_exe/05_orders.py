
















n_orders = int(input())

total_cost = 0

for order in range(n_orders):
    order_price = 0

    price_per_capsule = float(input())
    days = int(input())
    needed_capsule_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= needed_capsule_per_day <= 2000:
        order_price += price_per_capsule * days * needed_capsule_per_day
        total_cost += order_price

        print(f'The price for the coffee is: ${order_price:.2f}')

    else:
        continue

print(f'Total: ${total_cost:.2f}')
