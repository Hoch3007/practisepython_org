##### practicepython.org: Exercise 20

# Binary Search

import random

liste = random.sample(range(1,100,1), 99)

liste.sort()

n = 55

def binary_search(liste, n):    
    
    while len(liste)>1:

        l = len(liste)

        if n<liste[l/2]:

            liste = liste[0:l/2]

        else:

            liste = liste[l/2:]

        if len(liste)==1:    
            if n == liste[0]:
                print "Element ist in der Liste."
                print True

            else:
                print "Element ist nicht in der Liste."   
                print False

binary_search(liste, n)
