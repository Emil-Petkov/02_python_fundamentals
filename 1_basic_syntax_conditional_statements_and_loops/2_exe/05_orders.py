def calculate_order(n_orders):
    total_price = 0
    current_order = 0

    for _ in range(n_orders):
        price_per_capsule = float(input())
        days = int(input())
        needed_capsule_per_day = int(input())

        if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= needed_capsule_per_day <= 2000:

            calculate = (price_per_capsule * needed_capsule_per_day) * days
            current_order = calculate
            total_price += current_order
        else:
            continue

        print(f"The price for the coffee is: ${current_order:.2f}")

    print(f"Total: ${total_price:.2f}")


orders = int(input())
calculate_order(orders)
