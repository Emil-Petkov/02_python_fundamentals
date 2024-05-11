n_orders = int(input())

total = 0

for order in range(n_orders):
    price = float(input())
    days = int(input())
    capsule_per_day = int(input())

    if 0.01 <= price <= 100 and 1 <= days <= 31 and 1 <= capsule_per_day <= 2_000:
        current_order_price = price * days * capsule_per_day

        print(f'The price for the coffee is: ${current_order_price:.2f}')

        total += current_order_price

    continue

print(f'Total: ${total:.2f}')
