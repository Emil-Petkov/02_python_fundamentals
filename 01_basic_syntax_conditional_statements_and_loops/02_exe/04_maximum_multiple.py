






















divisor = int(input())
boundary = int(input())

largest_multiple = divisor * (boundary // divisor)

if largest_multiple > 0:
    print(largest_multiple)

else:
    print(divisor)
