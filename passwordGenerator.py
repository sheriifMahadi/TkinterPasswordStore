import random, string


password = []
characters = []

def passwordGenerator(length):
    """A function to generate strong random password"""

    for i in range(3):
        characters.append(random.choice(string.digits))
    for i in range(length-3):
        characters.append(random.choice(string.ascii_letters))


    if length < 8:
        passs = "Password too short."
        password.clear()
        characters.clear()
        return passs

    elif length > 20:
        passs = "length exceeded."
        password.clear()
        characters.clear()
        return passs

    else:
        random.shuffle(characters)
        for x in characters:
            password.append(x)
        passs = ( ''.join(password))
        password.clear()
        characters.clear()
        return passs
