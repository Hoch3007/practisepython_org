##### practicepython.org: Exercise 12

m = (np.random.rand(15)*10).astype(int).tolist()

def fila(m):
    
    n = [m[0], m[len(m)-1]]
    
    return n

fila(m)

m
