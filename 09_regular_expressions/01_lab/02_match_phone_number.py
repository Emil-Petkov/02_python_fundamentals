import re

pattern = r'\+359([ -])2\1\d{3}\1\d{4}\b'

text = input()

matches = re.finditer(pattern, text)

valid_numbers = [match.group() for match in matches]

print(", ".join(valid_numbers))
