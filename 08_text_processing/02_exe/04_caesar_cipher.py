text = input()
STEPS_FORWARD = 3
encrypted_text = ''

for ch in text:
    current_letter = ord(ch) + STEPS_FORWARD
    encrypted_text += chr(current_letter)

print(encrypted_text)
