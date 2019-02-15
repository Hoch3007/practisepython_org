##### practicepython.org: Exercise 4

x = range(2,11)

zahl5 = int(raw_input("Bitte nenn mir noch eine Zahl! "))

d = [i for i in x if zahl5%i==0]
print d
