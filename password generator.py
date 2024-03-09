import random
import string

def generate_password(length):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    all_chars = letters + numbers + symbols

    password = ""

    for i in range(length):
        password += random.choice(all_chars)

    return password

length = int(input("Enter length of password: "))

password = generate_password(length)

print(f"Generated password: {password}")
