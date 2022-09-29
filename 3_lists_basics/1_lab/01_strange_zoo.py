tail = input()
body = input()
head = input()

correct = [tail, body, head]

correct[0], correct[2] = correct[2], correct[0]

print(correct)
