##### practicepython.org: Exercise 14

def duplicates_set(liste):
    
    liste_neu = list(set(liste))
    
    return liste_neu

def duplicates_loop(liste):
    
    liste_neu = []
    
    for i in liste:
        
        if i not in liste_neu:
            liste_neu.append(i)
    
    return liste_neu

m = (np.random.rand(15)*10).astype(int).tolist()

duplicates_set(m)

duplicates_loop(m)
