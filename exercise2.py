##### practicepython.org: Exercise 2

zahl2 = int(raw_input("Bitte nenn mir noch eine Zahl! "))

if zahl2%4==0:
    print "Deine Zahl ist durch 4 teilbar."
elif zahl2%2==0:
    print "Deine Zahl ist gerade."
else:
    print "Deine Zahl ist ungerade."

zahl3 = int(raw_input("Bitte nenn mir noch eine Zahl! "))

if zahl2%zahl3==0:
    print "Deine Zahl "+str(zahl2)+ " ist durch die "+str(zahl3)+" teilbar."
else: 
    print "Die beiden Zahlen sind nicht durcheinander teilbar."
