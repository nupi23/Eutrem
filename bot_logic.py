import random

def gen_pass(pass_length = 8):
    elements = "+-/*!&$#?=@<>qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
