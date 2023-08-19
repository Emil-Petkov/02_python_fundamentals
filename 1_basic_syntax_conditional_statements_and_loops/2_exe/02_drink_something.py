def age_validator(age):
    if age <= 14:
        return "drink toddy"
    elif age <= 18:
        return "drink coke"
    elif age > 21:
        return "drink whisky"
    else:
        return "drink beer"


person_age = int(input())
print(age_validator(person_age))
