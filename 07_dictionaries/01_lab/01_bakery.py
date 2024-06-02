data = input().split()

store = {

}

for i in range(0, len(data), 2):
    key = data[i]
    value = data[i + 1]

    store[key] = int(value)

print(store)
