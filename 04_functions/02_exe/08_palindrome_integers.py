def palindrome_integers(numbers: list):
    for num in numbers:
        if num == num[::-1]:
            print('True')

        else:
            print('False')


sentence_of_numbers = input().split(', ')
palindrome_integers(sentence_of_numbers)
