##### practicepython.org: Exercise 23

happy = open('happynumbers.txt', 'r')
prime = open('primenumbers.txt', 'r')

happy_numbers = happy.readlines()

prime_numbers = prime.readlines()

overlap = []

for n in prime_numbers:
    
    if n in happy_numbers:
        overlap.append(n)
        
print overlap

for n in overlap:
    overlap.remove(n)
    n = n.rstrip()
    overlap.append(n)
print overlap

## funktioniert nicht so ganz, was aber auch nicht Teil der Aufgabe
