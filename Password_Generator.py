import string
import random

characters = string.ascii_letters + string.digits + \
    string.punctuation  # generating the set of characters
new_pw = ""  # Defining New Password as an empty String
# Requesting the size of the password
size = int(input("Provide the Size for the New Password: "))

while size != 0:
    size -= 1  # decreasing the size
    new_char = random.choice(characters)  # Picking up a charachter
    new_pw += new_char  # Concatening the new PW

print("The New Password is: ", new_pw)
