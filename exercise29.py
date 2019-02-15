##### practicepython.org: Exercise 29

def sieg(spiel):

    for i in range(3):

        #Zeilen
        if len(set(spiel[i]))==1 and spiel[i][0]!=0:
            print "Spieler "+ str(spiel[i][0]) + " hat gewonnen in Zeile: " + str(i+1)
            return spiel[i][0]

    for i in range(3):

        #Spalten
        if len(set([spiel[0][i], spiel[1][i], spiel[2][i]]))==1 and spiel[0][i]!=0:
            print "Spieler "+ str(spiel[0][i]) + " hat gewonnen in Spalte: " + str(i+1)
            return spiel[0][i]

    diag1 = set([spiel[0][0],spiel[1][1],spiel[2][2]])
    diag2 = set([spiel[0][2],spiel[1][1],spiel[2][0]])
    if len(diag1) == 1 or len(diag2) == 1 and spiel[1][1] != 0:
        print "Spieler "+ str(spiel[1][1]) + " hat gewonnen in einer Diagonale."
        return spiel[1][1]
    
    return 0

def brett(spiel):
    
    XO = {0: "-",1:"X", 2:"O"}
    spiel = [[XO[n] for n in l] for l in spiel]

    print " --- --- --- "
    print "| "+ str(spiel[0][0])+ " | "+ str(spiel[0][1])+" | "+str(spiel[0][2])+" |"
    print " --- --- --- "
    print "| "+ str(spiel[1][0])+ " | "+ str(spiel[1][1])+" | "+str(spiel[1][2])+" |"
    print " --- --- --- "
    print "| "+ str(spiel[2][0])+ " | "+ str(spiel[2][1])+" | "+str(spiel[2][2])+" |"
    print " --- --- --- "

def tictactoe():
    
    aktiver_spieler = 1
    spieler = 2
    spiel = [[0,0,0], [0,0,0], [0,0,0]]

    brett(spiel)
    counter = 0
    
    while sieg(spiel)==0 and counter<9:
    
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
        brett(spiel)

        temp = aktiver_spieler
        aktiver_spieler = spieler
        spieler= temp
        
        counter +=1
    
    if sieg(spiel)==0 and counter==9:
        
        print "Es ist ein Unentschieden."
    
    
    weiter = raw_input("Nochmal spielen? ja/nein ")
        
    if weiter =="ja":
        tictactoe()
    else:
        print "Vielen Dank für's Spielen!"

tictactoe()
