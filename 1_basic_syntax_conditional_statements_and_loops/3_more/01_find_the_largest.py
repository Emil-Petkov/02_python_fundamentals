number = input()

list_of_digits = []

for i in number:
    list_of_digits.append(i)

list_of_digits.sort(reverse=True)
########################################
digits = ""

for j in list_of_digits:
    digits += str(j)

integer = int(digits)

print(integer)
