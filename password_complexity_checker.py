import re

password = input("Enter password: ")

score = 0

if len(password) >= 8:
    score += 1

if re.search(r"[A-Z]", password):
    score += 1

if re.search(r"[a-z]", password):
    score += 1

if re.search(r"\d", password):
    score += 1

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

if score <= 2:
    print("Weak Password")
elif score == 3 or score == 4:
    print("Moderate Password")
else:
    print("Strong Password")
