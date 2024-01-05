#!/usr/bin/env python3

# Hangmang! by Sam Foster, 2022
#
# INSTRUCTIONS:
# You have been kidnapped by a gang of sadistic bibliophiles! They will let you
# live if you can correctly guess the letters in a secret word. But if you
# make 6 wrong guesses, you're dead! Will you survive the mercilessness?
#
# MORE INFORMATION:
# This is the classic Hangman game in Python 3. It uses ASCII graphics
# and should run on any platform that can run Python 3 with the random
# module. It has no dependencies, except for an included word list.
#
# This uses a list of words from the file: hangwords.txt
# The words list was obtained by taking the 1000 most common words in the
# English language (supposedly) and extracting only the 4 to 6-letter words.
# The words list was taken from: https://gist.github.com/deekayen/4148741

import random

# GRAPHICS!
hangManPicture = \
['''
      _____
     |     |
     |       
     |       
     |        
____/|\_______

''',
'''
      _____
     |     |
     |     O 
     |       
     |        
____/|\_______

''',
'''
      _____
     |     |
     |     O 
     |     | 
     |        
____/|\_______

''',
'''
      _____
     |     |
     |    _O 
     |     | 
     |        
____/|\_______

''',
'''
      _____
     |     |
     |    _O_
     |     | 
     |        
____/|\_______

''',
'''
      _____
     |     |
     |    _O_
     |     | 
     |    /   
____/|\_______

''',
'''
      _____
     |     |
     |    _O_
     |     | 
     |    / \\
____/|\_______
''']

freeMan = '''
          \O/   "Yahooo!!!"
           | 
          / \\
'''

# Funny things to say when the player is dead or about to lose.
deadPhrases = ["Oh, the humanity!", "Hasta la Vista, Baby!", "That's all, folks!"]
almostDeadPhrases = ["One more and you're dead!", "The kidnappers lick their chops.", "Say your prayers, varmint!", "You feel a chill run down your spine."]

# Returns a random 4-5 letter word to be used as the secret word.
# It takes a word list file as an input. Alternatively it could
# choose from a list object.
# It works by opening the file, reading the contents into a list,
# using random.choice() to pick a random item from the list,
# and then using the .strip() string method to remove any
# trailing newline character.
def newWord(filename):
    word = random.choice(list(open(filename))).strip()
    return word

# Draw the current board of the game.
# It requires the current guessed letters, partially filled in word,
# and number of bad guesses so far.
# There is not much to explain here - it's mostly print statements.
def drawBoard(wordFilledInList, guessedLettersList, guessCount):
    #print("")   # Print a blank line
    # Draw the hangman picture, based on the number of bad guesses so far
    print(hangManPicture[guessCount])
    # Draw the incomplete word so the user can guess
    print("The secret word is: ", end="")
    # Print each letter separated by spaces.
    print(" ".join(str(x) for x in wordFilledInList))
    print("")
    # Print the letters guessed so far
    print("Letters guessed so far: ", end="")
    for letter in guessedLettersList:
        print(letter, end=" ")
    print("")
    if guessCount == MAXGUESSES - 1:
        print("Bad guesses so far: " + str(guessCount) + "!", end=" ")
        print(random.choice(almostDeadPhrases))
    else:
        print("Bad guesses so far:", guessCount)
    print("")


# Update the partially filled in word on the board with the newest guess.
# Takes the currently guessed letter, the secret word, and the
# partially filled in word. Returns the updated partially filled in word.
def updateWordOnBoard(letter, word, wordFilledInList):
    for i in range(len(word)):
        if word[i] == letter:
            wordFilledInList[i] = letter
    return wordFilledInList

# Check and see if puzzle is solved.
# Do this by looking for remaining _ characters in wordFilledInList[]
def isPuzzleSolved(wordFilledInList):
    if '_' in wordFilledInList:
        return False
    else:
        return True

# Prompt user for the next letter to guess. 
# Check for valid input. if it's good, return it.
# If not, prompt the user again.
def askUserForLetter():
    inputValid = False
    # While we aren't happy with the input...
    while not inputValid:
        userInput = input("Guess a letter: ")
        if len(userInput) < 1:
            pass
        elif len(userInput) > 1:
            print("The kidnappers look at you disapprovingly. \"Just one letter, please.\"")
        elif len(userInput) == 1:   # Input is the right length.
            if userInput.isalpha(): # Is it a letter?
                inputValid = True
                letter = userInput.lower()
            elif userInput == "?":  # show help screen
                showInstructions()
                print("")
            else: # It's not a letter.
                print("The kidnappers poke you with a pointy stick. \"Just a letter, please.\"")
            
    return letter

# Tell the user how to play. A help screen.
def showInstructions():
    print("")
    print("You have been kidnapped by a gang of evil",
          "\nbibliophiles! They will let you live if",
          "\nyou can correctly guess all the letters",
          "\nin a secret word. But if you make 6 wrong",
          "\nguesses, you're dead! Will you survive",
          "\nthe mercilessness?")

# Start a game of Hangman! 
def playHangman():
    # Constants/configuration options
    WORDFILE="hangwords.txt"    # word list file
    global MAXGUESSES
    MAXGUESSES=6   # How many guesses will kill you?
    # end constants
    guessedLettersList = []
    wordFilledInList = []
    guessCount = 0

    # Start a new game
    word = newWord(WORDFILE)    # load a new word
    #print("SECRET: The word is:", word)
    for x in range(len(word)):
        wordFilledInList.append('_')

    # Main game loop.
    # As long as you aren't out of guesses or haven't solved the puzzle,
    # keep drawing the board, asking the user for guesses, and checking to see
    # if the guessed letter is in the word.
    while guessCount < MAXGUESSES and isPuzzleSolved(wordFilledInList) == False:
        drawBoard(wordFilledInList, guessedLettersList, guessCount)
        letter = askUserForLetter()
        print("")   # blank lines make things more readable
        if letter in guessedLettersList:
            print("You already guessed the letter " + letter + "!")
        # If the letter is a match...
        elif letter in word:
            # Update wordFilledInList
            wordFilledInList = updateWordOnBoard(letter, word, wordFilledInList)
            print("The letter '" + letter + "' IS in the word!")
            guessedLettersList.append(letter)
            pass
        else:
            print("The letter '" + letter + "' is NOT in the word!")
            guessCount += 1
            guessedLettersList.append(letter)
            guessedLettersList.sort()

    # The game is over!
    if isPuzzleSolved(wordFilledInList):    # did we win?
        print("The secret word is: ", end="")
        print(" ".join(str(x) for x in wordFilledInList))
        print(freeMan)
        print("Congratulations! You won! The secret word was:", word)
        if guessCount == 1:
            print("You only had 1 wrong guess! Not bad!")
        if guessCount == 0:
            print("You got a PERFECT score!! The kidnappers tip their hat to you as you scurry away.")
    else:
        print(hangManPicture[guessCount])
        print("You're dead! RIP!")
        print('"' + random.choice(deadPhrases) + '"')
        print("")
        print("The secret word was:", word)
    print(" ")  # print a blank line.

# Main Function - starts the game, then asks if the user wants to play again.
def main():
    print("Hangman!")
    userInput = input("Do you want instructions? ").lower()
    if len(userInput) > 0:
        if userInput[0] == "y":
            showInstructions()
    playingGame = True
    while playingGame:
        playHangman()
        userInput = input("Play again? ").lower()
        if len(userInput) > 0:
            if userInput[0] == "y":
                playingGame = True
            else:
                playingGame = False
        else:   # if the user just presses enter with no input.
            playingGame = False

main()

