##### practicepython.org: Exercise 11

def durch2(a):
    
    if a%2==0:
        return False
    else:
        return True

def durch3(a):
    
    if a%3==0:
        return False
    else:
        return True

def durch5(a):
    
    if a%5==0:
        return False
    else:
        return True

def durch7(a):
    
    if a%7==0:
        return False
    else:
        return True

def primzahl(a):
    
    liste = [durch2(a), durch3(a), durch5(a), durch7(a)]
    
    if False in liste:
        return False
    else:
        return True

def primzahlfrage():

    a = int(raw_input("Nenn mir eine Zahl! Ich prüfe ob es eine Primzahl ist. "))
    
    ergebnis= primzahl(a)
    
    if ergebnis == True:
        print "Die Zahl ist eine Primzahl."
        
    else:
        print "Die Zahl ist keine Primzahl."

primzahlfrage()
