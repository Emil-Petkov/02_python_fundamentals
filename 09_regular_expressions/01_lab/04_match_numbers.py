import re

pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'

text = input()

matches = re.findall(pattern, text)

numbers = [match[0] for match in re.finditer(pattern, text)]

print(" ".join(numbers))
