##### practicepython.org: Exercise 26

spiel =[[1,2,0], [0,2,1], [0,2,0]]

# Mit set als Funktion lässt sich ermitteln, ob in einer liste nur identische Elemente sind, dies ist der
# Fall, wenn die Liste aus set() nur ein Element hat.

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
        
    

sieg(spiel)
