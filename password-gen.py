import random

# total length of the password
length = 10

# collection of characters that can be used to generate the password
string = 'abcdefghijklmnopqrstuvwxyz12345678910ABCDEFGHIJKLMNOPQRSTUVWXYZ@!#'

# an empty password string
password_str = ''

# generating the string
for c in range(length):
    password_str += random.choice(string)

# displaying the generated password
print(password_str)
