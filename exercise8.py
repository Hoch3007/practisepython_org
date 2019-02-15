##### practicepython.org: Exercise 8

weiter = True

while weiter:
    
    string3 = str(raw_input("Spieler1: Stein? Schere? Papier? "))
    string4 = str(raw_input("Spieler2: Stein? Schere? Papier? "))
    
    if string3 ==string4:
        print "unentschieden"
    
    elif (string3=="Stein") & (string4=="Papier"):
        print "Spieler2 gewinnt."
    
    elif (string4=="Stein") & (string3=="Papier"):
        print "Spieler1 gewinnt."
    
    elif (string3=="Stein") & (string4=="Schere"):
        print "Spieler1 gewinnt."
    
    elif (string4=="Stein") & (string3=="Schere"):
        print "Spieler2 gewinnt."
    
    elif (string3=="Papier") & (string4=="Schere"):
        print "Spieler2 gewinnt."
    
    elif (string4=="Papier") & (string3=="Schere"):
        print "Spieler1 gewinnt."
    
    else:
        print "Bitte an die Regeln halten!"
    
    frage = str(raw_input("Weiter spielen? ja/nein "))
    
    if frage=="ja":
        weiter= True
    else:
        weiter=False
