##### practicepython.org: Exercise 3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for x in a:
    
    if x<=10:
        print x

b = [x for x in a if x<=10]

print b

zahl4 = int(raw_input("Bitte nenn mir noch eine Zahl! "))

c = [x for x in a if x<=zahl4]
print c
