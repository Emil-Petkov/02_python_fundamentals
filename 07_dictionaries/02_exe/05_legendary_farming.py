legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

obtained = False

while not obtained:
    line = input()
    parts = line.split()
    for i in range(0, len(parts), 2):
        quantity = int(parts[i])
        material = parts[i + 1].lower()

        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                obtained_item = legendary_items[material]
                print(f"{obtained_item} obtained!")
                key_materials[material] -= 250
                obtained = True
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity

for material in ["shards", "fragments", "motes"]:
    print(f"{material}: {key_materials[material]}")

for material, quantity in junk.items():
    print(f"{material}: {quantity}")
