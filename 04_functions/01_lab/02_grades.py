def grades(grade: float) -> float:
    if grade <= 2.99:
        return 'Fail'

    elif grade <= 3.49:
        return 'Poor'

    elif grade <= 4.49:
        return 'Good'

    elif grade <= 5.49:
        return 'Very Good'

    elif grade <= 6.00:
        return 'Excellent'


current_grade = float(input())

result = grades(current_grade)
print(result)
