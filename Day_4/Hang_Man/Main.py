import random
print ("                      ")
print ("    || Welcome to    ")
print ("                     ")
print ("       Hangman       ")

def convert(word):
    word = list(word.split(" "))
    return word


def Hangman_first ():
    print      ("           ----------")
    print      ("           |         ")
    print      ("           |         ")
    print      ("           |         ")

def Hangman_Second():
    print      ("           ----------")
    print      ("           |         ")
    print      ("           |         ")
    print      ("           |         ")
    print      ("         (^o^)       ")

def Hangman_Third():
    print      ("           ----------")
    print      ("           |         ")
    print      ("           |         ")
    print      ("           |         ")
    print      ("         (^o^)       ")
    print      ("          |||        ")

def Hangman_Fourth():
    print      ("           ----------")
    print      ("           |         ")
    print      ("           |         ")
    print      ("           |         ")
    print      ("         (^o^)       ")
    print      ("          |||        ")
    print      ("  *-----| | | |-----*")


def Hangman_Fifth():
    print      ("           ----------")
    print      ("           |         ")
    print      ("           |         ")
    print      ("           |         ")
    print      ("         (^o^)       ")
    print      ("          |||        ")
    print      ("  *-----| | | |-----*")
    print      ("         || ||       ")
    print      ("         || ||       ")

def Hangman_Sixth():
    print      ("           ----------")
    print      ("           |         ")
    print      ("           |         ")
    print      ("           |         ")
    print      ("         (^o^)       ")
    print      ("          |||        ")
    print      ("  *-----| | | |-----*")
    print      ("         || ||       ")
    print      ("         || ||       ")
    print      ("    _____|   |_____")

def Animals():
    Hangman_first()
    position = 0
    count = 0
    lives = 5
    Animals = ['Cheetah', 'Baboon', 'Cat', 'Dog', 'Lion', 'Monkey', 'Ape']
    word_value = random.randint(0, len(Animals)-1)
    word = Animals[word_value]
    length_word = len(word)
    blanks = '*' * length_word
    print (blanks)
    print (("The word is ") + str(length_word) + (" letters."))
    convert(blanks)
    while count < len(word):
        Letter = input("Input a letter:")
        if Letter in word:
            convert (word)
            count += 1
            print (Letter)
            while position < len(word):
                if word[position] == Letter:
                    blanks = blanks[:position] + Letter.upper() + blanks[position + 1:]
                position += 1
            str(word)
            print (blanks)
            word = word.replace(Letter," ")
            position = 0
        elif Letter not in word:
                lives -= 1
                if lives == 4:
                    Hangman_Second()
                elif lives == 3:
                    Hangman_Third()
                elif lives == 2:
                    Hangman_Fourth()
                elif lives == 1:
                    Hangman_Fifth()
                elif lives == 0:
                    Hangman_Sixth()
                    print ("GAME OVER. Press 'r' to restart")
                    restart = ("Restart?:")
                    if restart == "r" or restart == "R":
                        level_and_topic()
def Colors():
    Hangman_first()
    position = 0
    count = 0
    lives = 5
    Colors = ['Red', 'Blue', 'Magenta', 'Orange', 'Purple', 'Lavender', 'Violet']
    word_value = random.randint(0, len(Colors)-1)
    word = Colors[word_value]
    length_word = len(word)
    blanks = '*' * length_word
    print (blanks)
    print (("The word is ") + str(length_word) + (" letters."))
    convert(blanks)
    while count < len(word):
        Letter = input("Input a letter:")
        if Letter in word:
            convert (word)
            count += 1
            print (Letter)
            while position < len(word):
                if word[position] == Letter:
                    blanks = blanks[:position] + Letter.upper() + blanks[position + 1:]
                position += 1
            str(word)
            print (blanks)
            word = word.replace(Letter," ")
            position = 0
        elif Letter not in word:
                lives -= 1
                if lives == 4:
                    Hangman_Second()
                elif lives == 3:
                    Hangman_Third()
                elif lives == 2:
                    Hangman_Fourth()
                elif lives == 1:
                    Hangman_Fifth()
                elif lives == 0:
                    Hangman_Sixth()
                    print ("GAME OVER. Press 'r' to restart")
                    restart = ("Restart?:")
                    if restart == "r" or restart == "R":
                        level_and_topic()
def Numbers():
    Hangman_first()
    position = 0
    count = 0
    lives = 5
    Numbers = ['One', 'Three', 'Ten', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixty']
    word_value = random.randint(0, len(Numbers)-1)
    word = Numbers[word_value]
    length_word = len(word)
    blanks = '*' * length_word
    print (blanks)
    print (("The word is ") + str(length_word) + (" letters."))
    convert(blanks)
    while count < len(word):
        Letter = input("Input a letter:")
        if Letter in word:
            convert (word)
            count += 1
            print (Letter)
            while position < len(word):
                if word[position] == Letter:
                    blanks = blanks[:position] + Letter.upper() + blanks[position + 1:]
                position += 1
            str(word)
            print (blanks)
            word = word.replace(Letter," ")
            position = 0
        elif Letter not in word:
                lives -= 1
                if lives == 4:
                    Hangman_Second()
                elif lives == 3:
                    Hangman_Third()
                elif lives == 2:
                    Hangman_Fourth()
                elif lives == 1:
                    Hangman_Fifth()
                elif lives == 0:
                    Hangman_Sixth()
                    print ("GAME OVER. Press 'r' to restart")
                    restart = ("Restart?:")
                    if restart == "r" or restart == "R":
                        level_and_topic()

def Plants():
    Hangman_first()
    position = 0
    count = 0
    lives = 5
    Plants = ['Rose', 'Poision Ivy', 'Orchids', 'Conifers', 'Trees', 'Liverworts', 'Evergreens']
    word_value = random.randint(0, len(Plants)-1)
    word = Plants[word_value]
    length_word = len(word)
    blanks = '*' * length_word
    print (blanks)
    print (("The word is ") + str(length_word) + (" letters."))
    convert(blanks)
    while count < len(word):
        Letter = input("Input a letter:")
        if Letter in word:
            convert (word)
            count += 1
            print (Letter)
            while position < len(word):
                if word[position] == Letter:
                    blanks = blanks[:position] + Letter.upper() + blanks[position + 1:]
                position += 1
            str(word)
            print (blanks)
            word = word.replace(Letter," ")
            position = 0
        elif Letter not in word:
                lives -= 1
                if lives == 4:
                    Hangman_Second()
                elif lives == 3:
                    Hangman_Third()
                elif lives == 2:
                    Hangman_Fourth()
                elif lives == 1:
                    Hangman_Fifth()
                elif lives == 0:
                    Hangman_Sixth()
                    print ("GAME OVER. Press 'r' to restart")
                    restart = ("Restart?:")
                    if restart == "r" or restart == "R":
                        level_and_topic()

def Names():
    Hangman_first()
    position = 0
    count = 0
    lives = 5
    Names = ['Amanda', 'Devon', 'Catherine', 'David', 'Stephon', 'Sandra', 'Annie']
    word_value = random.randint(0, len(Names)-1)
    word = Names[word_value]
    length_word = len(word)
    blanks = '*' * length_word
    print (blanks)
    print (("The word is ") + str(length_word) + (" letters."))
    convert(blanks)
    while count < len(word):
        Letter = input("Input a letter:")
        if Letter in word:
            convert (word)
            count += 1
            print (Letter)
            while position < len(word):
                if word[position] == Letter:
                    blanks = blanks[:position] + Letter.upper() + blanks[position + 1:]
                position += 1
            str(word)
            print (blanks)
            word = word.replace(Letter," ")
            position = 0
        elif Letter not in word:
                lives -= 1
                if lives == 4:
                    Hangman_Second()
                elif lives == 3:
                    Hangman_Third()
                elif lives == 2:
                    Hangman_Fourth()
                elif lives == 1:
                    Hangman_Fifth()
                elif lives == 0:
                    Hangman_Sixth()
                    print ("GAME OVER. Press 'r' to restart")
                    restart = ("Restart?:")
                    if restart == "r" or restart == "R":
                        level_and_topic()

def Companies():
    Hangman_first()
    position = 0
    count = 0
    lives = 5
    Companies = ['McDonalds', 'Walmart', 'Target', 'Chick Fil A', 'IKea', 'Kroger', 'Starbucks']
    word_value = random.randint(0, len(Companies)-1)
    word = Companies[word_value]
    length_word = len(word)
    blanks = '*' * length_word
    print (blanks)
    print (("The word is ") + str(length_word) + (" letters."))
    convert(blanks)
    while count < len(word):
        Letter = input("Input a letter:")
        if Letter in word:
            convert (word)
            count += 1
            print (Letter)
            while position < len(word):
                if word[position] == Letter:
                    blanks = blanks[:position] + Letter.upper() + blanks[position + 1:]
                position += 1
            str(word)
            print (blanks)
            word = word.replace(Letter," ")
            position = 0
        elif Letter not in word:
                lives -= 1
                if lives == 4:
                    Hangman_Second()
                elif lives == 3:
                    Hangman_Third()
                elif lives == 2:
                    Hangman_Fourth()
                elif lives == 1:
                    Hangman_Fifth()
                elif lives == 0:
                    Hangman_Sixth()
                    print ("GAME OVER. Press 'r' to restart")
                    restart = ("Restart?:")
                    if restart == "r" or restart == "R":
                        level_and_topic()
def Countries():
    Hangman_first()
    position = 0
    count = 0
    lives = 5
    Countries = ['Malaysia', 'England', 'Cambodia', 'Vietnam', 'Korea', 'Bangladesh', 'Brazil']
    word_value = random.randint(0, len(Countries)-1)
    word = Countries[word_value]
    length_word = len(word)
    blanks = '*' * length_word
    print (blanks)
    print (("The word is ") + str(length_word) + (" letters."))
    convert(blanks)
    while count < len(word):
        Letter = input("Input a letter:")
        if Letter in word:
            convert (word)
            count += 1
            print (Letter)
            while position < len(word):
                if word[position] == Letter:
                    blanks = blanks[:position] + Letter.upper() + blanks[position + 1:]
                position += 1
            str(word)
            print (blanks)
            word = word.replace(Letter," ")
            position = 0
        elif Letter not in word:
                lives -= 1
                if lives == 4:
                    Hangman_Second()
                elif lives == 3:
                    Hangman_Third()
                elif lives == 2:
                    Hangman_Fourth()
                elif lives == 1:
                    Hangman_Fifth()
                elif lives == 0:
                    Hangman_Sixth()
                    print ("GAME OVER. Press 'r' to restart")
                    restart = ("Restart?:")
                    if restart == "r" or restart == "R":
                        level_and_topic()
def stars():
    Hangman_first()
    position = 0
    count = 0
    lives = 5
    stars = ['Polaris', 'Sirius', 'Betelguese', 'Vega', 'Rigel', 'Arcturus', 'Lyra']
    word_value = random.randint(0, len(stars)-1)
    word = stars[word_value]
    length_word = len(word)
    blanks = '*' * length_word
    print (blanks)
    print (("The word is ") + str(length_word) + (" letters."))
    convert(blanks)
    while count < len(word):
        Letter = input("Input a letter:")
        if Letter in word:
            convert (word)
            count += 1
            print (Letter)
            while position < len(word):
                if word[position] == Letter:
                    blanks = blanks[:position] + Letter.upper() + blanks[position + 1:]
                position += 1
            str(word)
            print (blanks)
            word = word.replace(Letter," ")
            position = 0
        elif Letter not in word:
                lives -= 1
                if lives == 4:
                    Hangman_Second()
                elif lives == 3:
                    Hangman_Third()
                elif lives == 2:
                    Hangman_Fourth()
                elif lives == 1:
                    Hangman_Fifth()
                elif lives == 0:
                    Hangman_Sixth()
                    print ("GAME OVER. Press 'r' to restart")
                    restart = ("Restart?:")
                    if restart == "r" or restart == "R":
                        level_and_topic()
def Science_Fiction():
    Hangman_first()
    position = 0
    count = 0
    lives = 5
    Science_Fiction = ['Doctor Who', 'Star Trek', 'Star Wars', 'Tardis', 'Enterprise', 'Phaser', 'Picard']
    word_value = random.randint(0, len(Science_Fiction)-1)
    word = Science_Fiction[word_value]
    length_word = len(word)
    blanks = '*' * length_word
    print (blanks)
    print (("The word is ") + str(length_word) + (" letters."))
    convert(blanks)
    while count < len(word):
        Letter = input("Input a letter:")
        if Letter in word:
            convert (word)
            count += 1
            print (Letter)
            while position < len(word):
                if word[position] == Letter:
                    blanks = blanks[:position] + Letter.upper() + blanks[position + 1:]
                position += 1
            str(word)
            print (blanks)
            word = word.replace(Letter," ")
            position = 0
        elif Letter not in word:
                lives -= 1
                if lives == 4:
                    Hangman_Second()
                elif lives == 3:
                    Hangman_Third()
                elif lives == 2:
                    Hangman_Fourth()
                elif lives == 1:
                    Hangman_Fifth()
                elif lives == 0:
                    Hangman_Sixth()
                    print ("GAME OVER. Press 'r' to restart")
                    restart = ("Restart?:")
                    if restart == "r" or restart == "R":
                        level_and_topic()


def level_and_topic():
    print ("Level One(press 1)")
    print ("Level Two(press 2)")
    print ("Level Three(press 3)")
    level = input("What level would like?")

    if level == "1":
        print ("Animals(Press A)")
        print ("Colors(Press C)")
        print ("Numbers(Press N)")
        topic = input("What topic would you like?:")
        if topic == 'A':
            Animals()
        elif topic == 'C':
            Colors()
        elif topic == 'N':
            Numbers()


    if level == "2":
        print ("Names(Press N)")
        print ("Plants(Press P)")
        print ("Companies(Press C)")
        topic = input("What topic would you like?:")
        if topic == "N":
            Names()
        elif topic == "P":
            Plants()
        elif topic == "C":
            Companies()

    if level == "3":
        print ("Countries(Press C)")
        print ("Stars(Press S)")
        print ("Science Fiction(Press S-F)")
        topic = input("What topic would you like?:")
        if topic == "C":
            Countries()
        elif topic == "S":
            stars()
        elif topic == "S-F":
            Science_Fiction()


level_and_topic()
