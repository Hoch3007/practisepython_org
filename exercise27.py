##### practicepython.org: Exercise 27

aktiver_spieler = 1
spieler = 2
spiel = [[0,0,0], [0,0,0], [0,0,0]]

print spiel

  
while sieg(spiel)==0:
    
    print "Spieler "+ str(aktiver_spieler) + " ist am Zug."
    zug = raw_input("Welches Feld soll besetzt werden? Eingabe als Zeile,Spalte. ")

    zug = zug.split(",")
    zeile = int(zug[0])-1
    spalte = int(zug[1])-1

    while spiel[zeile][spalte]>0:
        zug = raw_input("Das Feld ist belegt bitte neues Feld. Eingabe als Zeile,Spalte. ")
        zug = zug.split(",")
        zeile = int(zug[0])-1
        spalte = int(zug[1])-1

    spiel[zeile][spalte]=aktiver_spieler
    print spiel

    temp = aktiver_spieler
    aktiver_spieler = spieler
    spieler= temp
    
