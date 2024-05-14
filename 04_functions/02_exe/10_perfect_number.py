def is_perfect_number(num: int):
    if num <= 1:
        return 'It\'s not so perfect.'

    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i

    if divisors_sum == num:
        return 'We have a perfect number!'
    else:
        return 'It\'s not so perfect.'


number = int(input())
print(is_perfect_number(number))
