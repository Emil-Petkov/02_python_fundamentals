import re

total_cost = 0
furniture_list = []

pattern = r'>>(?P<name>[A-Za-z\s]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)'

while True:
    line = input()
    if line == "Purchase":
        break

    match = re.match(pattern, line)
    if match:
        name = match.group("name")
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))
        total_cost += price * quantity
        furniture_list.append(name)

print("Bought furniture:")

for furniture in furniture_list:
    print(furniture)

print(f"Total money spend: {total_cost:.2f}")
