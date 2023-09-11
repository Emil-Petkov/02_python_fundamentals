def convert_pounds_to_dollars(money):
    one_pound = 1.31

    return f"{money * one_pound:.3f}"


money = int(input())

print(convert_pounds_to_dollars(money))
