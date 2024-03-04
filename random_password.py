import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

length=int(input("Enter length of password to generate:"))
password = generate_password(length)
print("Generated Password:", password)
