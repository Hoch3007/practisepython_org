##### practicepython.org: Exercise 33

def get_birthday(name):
    
    return birthdays.get(name, "not in list")

if __name__ == "__main__":
    
    birthdays = {"Benjamin Banneker": "November 9, 1731",
                 "Charles Drew": "3 June 1904", 
                 "Dr. Daniel Hale Williams":"January 18, 1858",
                 "Emmett Chappelle": "October 25, 1925",
                 "Ernest Everett Just":"August 14, 1883", 
                 "Garrett Morgan": "March 4, 1877"}
    
    name = raw_input("Which birthday would you like to know? ")
    
    date = get_birthday(name)
    
    print name+"s birthday is " + str(date)+ "."

##### practicepython.org: Exercise 34

def ask():

    with open("birthdays.json", "r") as f:
        birthdays = json.load(f)

    name = raw_input("Which birthday would you like to know? ")

    date = get_birthday(name)

    if date == "not in list":
        print "The birthday is not in the list."
        addition = raw_input("Would you like to add the birthday? y/n ")
        if addition=="y":
            addition = raw_input("When is "+ name +"s birthday? ")
            birthdays[name]=addition
            print "The Birthday was saved."
            with open("birthdays.json", "w") as f:
                json.dump(birthdays, f)
    else:
        print name+"s birthday is " + str(date)+ "."
    
    next_one = raw_input("Would you like to know anther birthday? y/n ")
    
    if next_one=="y":
        ask()
    else:
        print "Thanks for using the birthday list!"
        

if __name__ == "__main__":

    import json
    
    ask()
