import re
import sys

pattern = r'\b_([A-Za-z0-9]+)\b'

variables = []

for line in sys.stdin:
    matches = re.findall(pattern, line)
    variables.extend(matches)

print(','.join(variables))
