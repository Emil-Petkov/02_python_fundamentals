





















data = input().split(': ')

products = {

}

while not data[0] == 'statistics':
    product = data[0]
    quantity = data[1]

    if product in products:
        products[product] += int(quantity)
    else:
        products[product] = int(quantity)

    data = input().split(': ')

print('Products in stock:')

for key, value in products.items():
    print(f'- {key}: {value}')

print(f'Total Products: {len(products.keys())}\nTotal Quantity: {sum(products.values())}')
