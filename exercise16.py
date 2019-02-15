##### practicepython.org: Exercise 16
einfacher Passwort-Generator

import random
import string

def password(p):

    lower = list(string.ascii_lowercase)

    upper = list(string.ascii_uppercase)

    digits = list(string.digits)

    punctuation = list(string.punctuation)

    liste = [lower, upper, digits, punctuation]

    password = []

    for i in range(p):

        auswahl = random.choice(liste)
        character = random.choice(auswahl)

        password.append(character)

    password = "".join(password)
    
    return password

def main():
    
    p = int(raw_input("Wie lang soll dein Passwort sein? min. 6 Zeichen "))
    
    x = password(p)
    
    print "Dein Passwort lautet: "
    print x

if __name__ == "__main__":
    main()
