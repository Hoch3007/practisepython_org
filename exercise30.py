##### practicepython.org: Exercise 30

def random_word():
    
    import random

    with open('sowpods.txt', 'r') as f:
        line = f.readlines()

    lines = [l.strip("\r\n") for l in line]

    position = random.randint(0, len(lines)-1)  
    
    return lines[position]

random_word()
