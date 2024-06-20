data = input().split()
order = {}

while not data[0] == 'buy':
    product = data[0]
    price = float(data[1])
    quantity = int(data[2])

    if product not in order:
        order[product] = [price, quantity]

    else:
        order[product][1] += quantity
        order[product][0] = price

    data = input().split()

for product, v in order.items():
    total_price = v[0] * v[1]
    print(f'{product} -> {total_price:.2f}')
