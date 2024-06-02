data = input().split()
search_products = input().split()

products = {

}

for p in range(0, len(data), 2):
    key = data[p]
    value = data[p + 1]

    products[key] = int(value)

for product in search_products:
    if product in products:

        print(f'We have {products[product]} of {product} left')

    else:
        print(f'Sorry, we don\'t have {product}')
