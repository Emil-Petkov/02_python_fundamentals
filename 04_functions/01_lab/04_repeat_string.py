def repeat_string(text: str, count: int):
    return text * count


text = input()
count = int(input())
result = repeat_string(text, count)
print(result)
