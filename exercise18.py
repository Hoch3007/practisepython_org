##### practicepython.org: Exercise 18

def zahl_test(n, zahl):
    
    n=str(n)
    zahl = str(zahl)
    
    cows = 0
    bulls=0
    
    for i in range(len(n)):   
        
        if n[i] in zahl:
            bulls+=1
            if n[i]==zahl[i]:
                cows+=1
                bulls-=1
                
    print str(cows) + " cows, " + str(bulls) + " bulls"
    
    return cows, bulls

def game():
    
    print "Cows & Bulls - Ein Ratespiel"
    print "----------------------------"
    print "Cows: Richtige Zahl am richtigen Platz"
    print "Bulls: Richtige Zahl am falschen Platz"
    print "----------------------------"
    
    import random
    
    zahl = random.randint(1000,10000)
    
    n = int(raw_input("Nenn eine Zahl zwischen 1000 und 9999! "))
    
    ergebnis = zahl_test(n, zahl)
    
    while ergebnis[0]<4:
        
        weiter = (raw_input("Willst du weiter raten? ja/nein "))
        
        if weiter == "nein":
            print "Schade, die richtige Zahl war: " + str(zahl)
            break
            
        n = int(raw_input("Korrigiere deinen Versuch! Wie lautet die Zahl? "))
    
        ergebnis = zahl_test(n, zahl)
    
    if n == zahl:
        print "Sehr gut, deine Zahl ist korrekt. Die Lösung lautet " + str(zahl) + "."

if __name__ == "__main__":
    game()
