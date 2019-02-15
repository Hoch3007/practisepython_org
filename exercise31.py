##### practicepython.org: Exercise 31

def hangman():
    
    print "Welcome to Hangman!"
    
    word = random_word()
    length = len(word)
    print "_ "*length
    positions=[]
    
    game(word, length, positions)
    

def game(word, length, positions):
    guess = raw_input("Guess a letter: ")
    guess = guess.upper()
    
    if guess in word:
        new = [pos for pos, char in enumerate(word) if char == guess]
        
        for n in new:
            positions.append(n)
        
    else:
        print "Not in word!"
    
    counter = 0
    for i in range(length):

        if i in positions:
            counter +=1
            print word[i] + " ", 
        else:
            print "_ ",
    
    if counter== length:
        print "You won!"
    else:
        weiter = raw_input("Guess again? y/n ")
    
    if weiter =="y":
        game(word, length, positions) 
    else:
        print "The word was " + word + "."
        print "Thanks for playing!"

hangman()
