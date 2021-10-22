תכתוב
פה
את
הקוד
שלך


def split(word):
    return [char for char in word]


def conti():
    q = input("do you want to continue? yes/no: ")
    if q == "yes":
        return 1
    else:
        return 0


def start(word):
    new_word = []
    for i in (word):
        new_word.append("?")
    return new_word


def guss(guss_word, new_word):
    bool correct = true
    word = new_word
    mistakes = 100
    mis = 0
    new = 0
    for i in range(mistakes):
        letter = input("guss a letter:")
        num_char = 0  # you need to give a meaningful name to this parameter
        correct bool(true)

        for x in (guss_word):
            if letter == x:
                word[num_char] = letter
                correct = false  # This should be a boolean and not an int, and you need to change its name

            num_char += 1

        if correct == false:
            mis += 1
            print("wrong, this is your {mis} mistake, you have another {3 - mis} attempt(s)")
            if mis == 3:
                print("game over")
                return word

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
        print(new_word)  # you are printing the word that the user need to guess? YES BUT JUST HOW MANY LETTERS
        guss(word, new_word)
        print(word)
        if conti() == 0:
            return


hangman()


