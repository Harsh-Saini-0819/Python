import random       # gives random value
import string       # Collection of string constant

pass_len = 12
values = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(pass_len):
    password += random.choice(values)
    
print("Your generated password : ",password)