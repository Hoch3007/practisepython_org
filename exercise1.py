##### practicepython.org: Exercise 1

import datetime

## bei Python 2.7 ist es raw_input, das wurde ab 3.3 zu input

name = raw_input("Wie heißt du? ")
alter = int(raw_input("Wie alt bist du? "))

now = datetime.datetime.now()
hundert = now.year+(100-alter)

print "Hallo Peter, im Jahr "+ str(hundert)+ " wirst du 100 Jahre alt sein."

zahl = int(raw_input("Nenn mir eine Zahl!"))

for i in range(zahl):
    print "Hallo Peter, im Jahr "+ str(hundert)+ " wirst du 100 Jahre alt sein."
