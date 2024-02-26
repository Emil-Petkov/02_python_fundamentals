start_index = int(input())
end_index = int(input())

symbols = ''

for ch in range(start_index, end_index + 1):
    symbols += chr(ch)

print(' '.join(symbols))
