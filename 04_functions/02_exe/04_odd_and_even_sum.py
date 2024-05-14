def odd_and_even_sum(number: str):
    even_sum = 0
    odd_sum = 0

    for num in number:
        if int(num) % 2 == 0:
            even_sum += int(num)

        else:
            odd_sum += int(num)

    return even_sum, odd_sum


number = input()
even, odd = odd_and_even_sum(number)
print(f'Odd sum = {odd}, Even sum = {even}')
