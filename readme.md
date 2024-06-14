# Hangmang!
by Sam Foster. 2022

## INSTRUCTIONS:

You have been kidnapped by a gang of sadistic bibliophiles! They will let
you live if you can correctly guess the letters in a secret word. But if
you make 6 wrong guesses, you're dead! Will you survive the mercilessness?

## MORE INFORMATION:

This is the classic Hangman game in Python 3. It uses ASCII graphics
and should run on any platform that can run Python 3 with the random
module. It has no dependencies, except for an included word list.

Its <40 column ASCII graphics make it suitable for playing on machines
as humble as a teletype/teleprinter, or an Apple II (as, say, a serial
terminal). This is the kind of game you can play from a 50 year old
mainframe console, or an IBM-PC with MDA.

This uses a list of words from the file: hangwords.txt

The words list was obtained by taking the 1000 most common words in the
English language (supposedly) and extracting only the 4 to 6-letter words.
The words list was taken from: https://gist.github.com/deekayen/4148741

Example game:

```

% ./hangman.py
Hangman!
Do you want instructions? y

You have been kidnapped by a gang of evil
bibliophiles! They will let you live if
you can correctly guess all the letters
in a secret word. But if you make 6 wrong
guesses, you're dead! Will you survive
the mercilessness?

      _____
     |     |
     |
     |
     |
____/|\_______


The secret word is: _ _ _ _ _ _

Letters guessed so far:
Bad guesses so far: 0

Guess a letter: e

The letter 'e' IS in the word!

      _____
     |     |
     |
     |
     |
____/|\_______


The secret word is: _ _ _ e _ _

Letters guessed so far: e
Bad guesses so far: 0

Guess a letter: a

The letter 'a' is NOT in the word!

      _____
     |     |
     |     O
     |
     |
____/|\_______


The secret word is: _ _ _ e _ _

Letters guessed so far: a e
Bad guesses so far: 1

Guess a letter: o

The letter 'o' IS in the word!

      _____
     |     |
     |     O
     |
     |
____/|\_______


The secret word is: _ o _ e _ _

Letters guessed so far: a e o
Bad guesses so far: 1

Guess a letter: l

The letter 'l' is NOT in the word!

      _____
     |     |
     |     O
     |     |
     |
____/|\_______


The secret word is: _ o _ e _ _

Letters guessed so far: a e l o
Bad guesses so far: 2

Guess a letter: n

The letter 'n' IS in the word!

      _____
     |     |
     |     O
     |     |
     |
____/|\_______


The secret word is: _ o _ e _ n

Letters guessed so far: a e l o n
Bad guesses so far: 2

Guess a letter: s

The letter 's' is NOT in the word!

      _____
     |     |
     |    _O
     |     |
     |
____/|\_______


The secret word is: _ o _ e _ n

Letters guessed so far: a e l n o s
Bad guesses so far: 3

Guess a letter: l

You already guessed the letter l!

      _____
     |     |
     |    _O
     |     |
     |
____/|\_______


The secret word is: _ o _ e _ n

Letters guessed so far: a e l n o s
Bad guesses so far: 3

Guess a letter: laksjdf
The kidnappers look at you disapprovingly. "Just one letter, please."
Guess a letter: 3
The kidnappers poke you with a pointy stick. "Just a letter, please."
Guess a letter: v

The letter 'v' IS in the word!

      _____
     |     |
     |    _O
     |     |
     |
____/|\_______


The secret word is: _ o v e _ n

Letters guessed so far: a e l n o s v
Bad guesses so far: 3

Guess a letter: g

The letter 'g' IS in the word!

      _____
     |     |
     |    _O
     |     |
     |
____/|\_______


The secret word is: g o v e _ n

Letters guessed so far: a e l n o s v g
Bad guesses so far: 3

Guess a letter: r

The letter 'r' IS in the word!
The secret word is: g o v e r n

          \O/   "Yahooo!!!"
           |
          / \

Congratulations! You won! The secret word was: govern

Play again?

```

