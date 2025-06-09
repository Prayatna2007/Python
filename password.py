import random
import string

l=int(input("Enter the length for password:"))
def generate_password(length=l):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password
print("The password is: \t",generate_password())
