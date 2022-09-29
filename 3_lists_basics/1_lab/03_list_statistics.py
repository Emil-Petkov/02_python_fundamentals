numbers = int(input())

positive_numbers = []
count_positive = 0
negative_numbers = []
sum_of_negative = 0

for i in range(numbers):
    current_number = int(input())
    if current_number >= 0:
        positive_numbers.append(current_number)
        count_positive += 1
    else:
        negative_numbers.append(current_number)
        sum_of_negative += current_number

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {count_positive}")
print(f"Sum of negatives: {sum_of_negative}")
