# Password Strength Checker - Cybersecurity Project

password = input("Enter a password: ")

score = 0

# Length check
if len(password) >= 8:
    score += 1

# Uppercase check
if any(char.isupper() for char in password):
    score += 1

# Lowercase check
if any(char.islower() for char in password):
    score += 1

# Number check
if any(char.isdigit() for char in password):
    score += 1

# Special character check
special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
if any(char in special_chars for char in password):
    score += 1

# Result
if score == 5:
    print("Strong password")
elif score >= 3:
    print("Medium strength password")
else:
    print("Weak password")
