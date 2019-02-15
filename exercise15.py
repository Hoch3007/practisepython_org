##### practicepython.org: Exercise 15

def rueckwaerts():
    
    p = raw_input("Nenn mir einen Satz und ich drehe ihn um! ")
    
    s = p.split()
    s.reverse()
    
    new_string = " ".join(s)
    
    return new_string

rueckwaerts()
