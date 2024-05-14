def orders(product: str, quantity: int):
    price = {
        'coffee': 1.50,
        'water': 1.00,
        'coke': 1.40,
        'snacks': 2.00,
    }

    if product in price:
        return price[product] * quantity


product = input()
quantity = int(input())
result = orders(product, quantity)
print(f'{result:.2f}')
