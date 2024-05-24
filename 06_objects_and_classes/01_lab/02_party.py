class Party:
    def __init__(self):
        self.peoples = []


party = Party()

command = input()
while not command == 'End':
    current_name = command
    party.peoples.append(current_name)

    command = input()

print(f'Going: {", ".join(party.peoples)}')
print(f'Total: {len(party.peoples)}')
