def split(word):
    return [char for char in word]


def conti():
    q = input("do you want to continue? yes/no: ")
    if q == "yes":
        return 1
    else:
        return 0

def allready_try(letter, letter_exist):
    exist = letter_exist
    for i in (letter_exist):
        if letter == i:
            print("you allready tried this letter, try again")
            break
    letter_exist = exist.append(letter)
    return letter, letter_exist



def start(word):
    new_word = []
    for i in (word):
        new_word.append("?")
    return new_word


def guss(guss_word, new_word):
    word = new_word
    mistakes = 100
    mis = 0
    letter_exist = [""]
    for i in range(mistakes):
        letter = input("guss a letter:")
        allready_try(letter, letter_exist)
        num_char = 0
        correct = False

        for x in (guss_word):
            if letter == x:
                word[num_char] = letter
                correct = True
            num_char += 1

        if False == correct:
            mis += 1
            if 3 == mis:
                print("game over")
                return word
            print(f"wrong, this is your {mis} mistake, you have another {3 - mis} attempt(s)")

        else:
            print(word)

        if word == guss_word:
            print("well done")
            mis = 0
            return word


def hangman():
    choosen_words = ["banana", "watermalone", "baloon", "television", "basketball"]
    for i in (choosen_words):
        word = split(i)
        new_word = start(i)
        print(new_word)
        guss(word, new_word)
        print(word)
        if conti() == 0:
            return


hangman()


