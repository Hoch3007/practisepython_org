##### practicepython.org: Exercise 10

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def doppelte(a, b):
    
    c = [x for x in a if x in b]
    d=[]
    
    for y in c:
        if y not in d:
            d.append(y)
    
    return d

doppelte(a,b)

a = (np.random.rand(10)*10).astype(int).tolist()

b = (np.random.rand(15)*10).astype(int).tolist()

doppelte(a,b)
