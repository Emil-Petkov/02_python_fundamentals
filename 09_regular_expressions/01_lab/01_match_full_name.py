import re

pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

text = input('')

matches = re.findall(pattern, text)

for match in matches:
    print(match, end=' ')
