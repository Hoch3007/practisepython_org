##### practicepython.org: Exercise 25

print "Denk dir eine Zahl zwischen 0 und 100! Ich werde sie erraten."

print "Es ist die 50."

info = raw_input("Zu hoch oder zu niedrig oder stimmt? ")

n = 50
liste = range(0,100)

start = 0
ende = 50
counter = 0

while info !="stimmt":
    
    counter +=1
    if info=="zu hoch":
       
        start = liste.index(liste[0])
        ende =  liste.index(n)+1
        
        liste = liste[start:ende]
        #print liste
        
    else:

        start = liste.index(n)+1
        ende =  liste.index(liste[len(liste)-1])
        
        liste = liste[start:ende]
        #print liste
        
    if len(liste)==2:    
        liste.remove(n)
        n = liste[0]
    else:    
        n = liste[len(liste)/2]

    print "Es ist die " + str(n) + "."

    info = raw_input("Zu hoch oder zu niedrig oder stimmt? ")

print "Das Erraten der Zahl dauerte " + str(counter) + " Versuche."
