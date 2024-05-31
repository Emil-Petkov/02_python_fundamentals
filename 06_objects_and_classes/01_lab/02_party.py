class Party:
    def __init__(self):
        self.guests = []


party = Party()

command = input()

while not command == 'End':
    party.guests.append(command)

    command = input()

print(f"Going: {', '.join(party.guests)}\nTotal: {len(party.guests)}")
