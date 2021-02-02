import random

wordsdb = ["water", "airplane", "love", "robot", "animal"]

def keep_playing(currentLives, wordSlctd, blankSpaces):
    print("try to guess typing a single letter, you have {} attempts remaining" .format(currentLives))
    charToGuess = input("What is your letter? \n -")
    check_if_char(blankSpaces, wordSlctd, charToGuess, currentLives)

def hangItUp(hp, wordSlctd, blankSpaces):
    hp -= 1
    print("Your character is not on the string. Hanging him up!")
    print("{} attempts remaining " .format(hp))
    if hp <= 0:
        print("Its over, the actual word was : {} " .format(wordSlctd))
        userResponse = input("Game Over! Waiting for your response...")
        if userResponse == "try again":
            print("restarting the game.")
        else:
            print("Bye bye...")
    else:
        keep_playing(hp, wordSlctd, blankSpaces)
    return hp

def revealWord(blankSpaces, letterToReveal, wordPosition, actualString):
    blankSpaces = list(blankSpaces)
    countChar = len(actualString)
    dividedString = list(actualString)
    chara = letterToReveal
    joinWord = []

    y = 0
    while y < countChar:
        y += 1
        if letterToReveal == dividedString[y - 1]:
            print("matched")
            blankSpaces[y - 1] = letterToReveal

    joinWord = "".join(blankSpaces)
    return joinWord

def check_if_char(blankSpaces, ogWord, selectedChar, currentLives):
    revealedWord = blankSpaces
    countChar = len(ogWord)
    wordSplitted = list(ogWord)
    wordCount = wordSplitted.count(selectedChar)
    matchedIndexes = []

    if selectedChar in wordSplitted:
        x = 0
        while x < countChar:
            x += 1
            if selectedChar == wordSplitted[x - 1]:
                matchedIndexes.append(x)

        print("You guessed right! Your letter -{}- is #{} time/s in the original word" .format(selectedChar, wordCount))
        revealedWord = revealWord(blankSpaces, selectedChar, matchedIndexes, ogWord)

        print("your word now looks like this: --- {} ---" .format(revealedWord))
        if ogWord == revealedWord:
            print("...and that was the word!")
            print("Congratulations!!! You won the game")
        else:
            keep_playing(currentLives, ogWord, revealedWord)
    else:
        print("your current word: --- {} ---" .format("".join(blankSpaces)))
        currentLives = hangItUp(currentLives, ogWord, revealedWord)
        keep_playing(currentLives, ogWord, revealedWord)

def check_if_guessed(lettersGuessed, letterSelected):

    if letterSelected in lettersGuessed:
        print("oops! you already tried that word, nothing happened!")
        return True
    else:
        return False

def hangman_game():
    lettersGuessed = []
    lives = 6
    theSelectedWord = random.choice(wordsdb)
    countTheBlankSpaces = len(theSelectedWord)
    theBlankSpaces = []


    for i in range(countTheBlankSpaces):
        theBlankSpaces.append("_")

    print("your word kinda looks like this: {} " .format(" ".join(theBlankSpaces)))
    keep_playing(lives, theSelectedWord, theBlankSpaces)

hangman_game()
