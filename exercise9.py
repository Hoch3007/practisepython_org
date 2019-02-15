##### practicepython.org: Exercise 9

import random

zahl = random.randint(0,10)

weiter = True
raten = int(raw_input("Ich habe mir eine Zahl überlegt. Wie lautet sie? "))

while weiter:
    
    if zahl<raten:
        weiter = raw_input("Deine Zahl war zu hoch. Willst du weiter raten? ja/nein ")
        
        if weiter =="ja":
            raten = int(raw_input("Dann gib eine neue Zahl ein!"))
        
        else:
            print "Alles klar. Vielen Dank fürs Spielen!"
            weiter= False
    
    elif zahl >raten:
        
        weiter = raw_input("Deine Zahl war zu niedrig. Willst du weiter raten? ja/nein ")
        
        if weiter =="ja":
            raten = int(raw_input("Dann gib eine neue Zahl ein!"))
        
        else:
            print "Alles klar. Vielen Dank fürs Spielen!"
            weiter= False
    
    else:
        print "Genau richtig! Vielen Dank fürs Spielen"
        weiter=False
