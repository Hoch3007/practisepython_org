##### practicepython.org: Exercise 6

string1 = str(raw_input("Bitte nenn mir ein Wort! "))

s = len(string1)

string1=string1.lower()

string2=''.join(reversed(string1))

if string1 == string2:
    print "Wort ist ein Palindrom."
else:
    print "Wort ist kein Palindrom."
    
