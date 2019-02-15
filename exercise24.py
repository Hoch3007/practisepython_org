##### practicepython.org: Exercise 24

def spielbrett(zeile, spalte):

    if spalte >1:
        print '|---', 
    else:
        print '|---|', 

    if spalte > 2:

        for i in range(spalte-2):
            print '| ---',

        print '| --- |'

    else: 

        for i in range(spalte-2):
            print '| --- |',

        print '| --- |'


    for z in range(zeile):    

        if spalte >1:
            print '|   ', 
        else:
            print '|   |', 

        if spalte > 2:

            for i in range(spalte-2):
                print '|    ',

            print '|     |'

        else: 

            for i in range(spalte-2):
                print '|     |',

            print '|     |'

        if spalte >1:
            print '|---', 
        else:
            print '|---|', 

        if spalte > 2:

            for i in range(spalte-2):
                print '| ---',

            print '| --- |'

        else: 

            for i in range(spalte-2):
                print '| --- |',

            print '| --- |'


spielbrett(3,3)
