import re

text = input()
word = input().strip()

pattern = rf'\b{re.escape(word)}\b'

matches = re.findall(pattern, text, re.IGNORECASE)

print(len(matches))
