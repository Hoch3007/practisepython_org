##### practicepython.org: Exercise 13

def fibonacci(p):
    
    if p >2:
        return fibonacci(p-1)+fibonacci(p-2)
    else:
        return 1

def fibonacci_frage():
    
    p = int(raw_input("Wieviele Fibonacci-Zahlen sollen berechnet werden? "))
    
    liste = []
    
    for x in range(1,p+1,1):
        
        liste.append(fibonacci(x))
    
    print "Dies sind deine Fibonacci-Zahlen: "
    print liste

fibonacci_frage()
