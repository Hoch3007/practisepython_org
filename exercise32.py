##### practicepython.org: Exercise 32

def random_word2():
    
    import random

    with open('sowpods.txt', 'r') as f:
        line = f.readlines()

    lines = [l.strip("\r\n") for l in line]

    position = random.randint(0, len(lines)-1)  
    
    return lines[position]

def hangman2():
    
    print "Welcome to Hangman!"
    print "-------------------"
    print "You have six tries to guess the word."
    
    start()
    
    print "Thanks for playing!"

def start():
    word = random_word2()
    length = len(word)
    print "_ "*length
    positions=[]
    
    guesses = 0
    
    game2(word, length, positions, guesses)

def play_again():
    
    neu = raw_input("Play again? y/n ")
        
    if neu =="y":
        start()

def game2(word, length, positions, guesses):
    
    guess = raw_input("Guess a letter: ")
    
 
    guess = guess.upper()
    guesses+=1
    if guess in word:
        new = [pos for pos, char in enumerate(word) if char == guess]
        
        for n in new:
            positions.append(n)
        
    else:
        print "Not in word!"
    
    print "You have "+ str(6-guesses) + " left."
    
    counter = 0
    for i in range(length):

        if i in positions:
            counter +=1
            print word[i] + " ", 
        else:
            print "_ ",
    
    if counter== length:
        print "You won!"
        play_again()
    elif guesses ==6:
        print "You lost. This was your sixth guess."
        print "The word was " + word + "."
        play_again()
    else:
        weiter = raw_input("Guess again? y/n ")
    
        if weiter =="y":
            game2(word, length, positions, guesses) 
        else:
            print "The word was " + word + "."
            play_again()

            
if __name__ == '__main__':
    hangman2()
