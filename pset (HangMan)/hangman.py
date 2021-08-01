# Problem Set 2, hangman.py
# Name: Muhammad Hammad Faisal
# Collaborators: None

# Hangman Game
# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

# choosing random word
def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    word = random.choice(wordlist)
    return word

# -----------------------------------
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for alpha in secret_word:
        if alpha not in letters_guessed:
            return False

    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    stringofwords = ' '
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            stringofwords = stringofwords+' '+secret_word[i]
        else:
            stringofwords = stringofwords + ' _ '
    return stringofwords

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase
    for i in range(len(letters_guessed)):
        if letters_guessed[i] in letters:
            letters = letters.replace(letters_guessed[i], '')
    return letters

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the Game Hangman!")
    print("I am thinking of a word which is",len(secret_word),'long')
    print("--------------------")
    Guesses = 6
    Warnings = 3
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'u', 'o']
    while Guesses > 0 and is_word_guessed(secret_word,letters_guessed) == False:
        print("You have", Warnings, 'Warnings left.')
        print("You have",Guesses,'guesses left.')
        print("Available Letters:",get_available_letters(letters_guessed))
        guess = input('Please guess a letter:')
        guess = guess.strip().lower()
        if guess in secret_word:
            if guess in letters_guessed:
                if Warnings > 0:
                    Warnings -= 1
                    print("Oops! You have already guessed that letter. You now have",Warnings,"Warnings left"
                                                                                              "\n Word: ",get_guessed_word(secret_word,letters_guessed))
                else:
                    Guesses -=1
                    print("Oops! You have already guessed that letter. Word:",get_guessed_word(secret_word, letters_guessed))
            elif guess not in letters_guessed:
                letters_guessed.append(guess)
                print('Good Guess!',get_guessed_word(secret_word,letters_guessed))
        elif guess.isalpha() == False or len(guess) != 1:
            if Warnings > 0:
                Warnings -= 1
                print("Oops! That is not a valid letter. You have", Warnings, "Warnings left.\n Word:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                Guesses -= 1
                print("Oops! That is not a valid letter. Word:",
                      get_guessed_word(secret_word, letters_guessed))
        elif guess in vowels:
            for vowel in vowels:
                if vowel not in secret_word:
                    Guesses -= 2
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            Guesses -= 1
        print("--------------------")
    if is_word_guessed(secret_word,letters_guessed) == True:
        print("Congratulations, You Won!")
        print("Your Score is", Guesses * len(secret_word))
    elif is_word_guessed(secret_word,letters_guessed) == False:
        print("Sorry! you ran out of guesses. The word was", secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word = my_word.replace(' ','')

    if len(other_word) == len(my_word):
        for i in range(len(my_word)):
            if my_word[i] == other_word[i]:
                continue
            if my_word[i] == '_' and other_word[i] not in list(my_word):
                continue
            else:
                return False
        return True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    words = ""
    count =0
    for word in wordlist:
        if count % 5 == 0:
            words += '\n'
        if match_with_gaps(my_word,word):
            words += word +" "
            count += 1
        else:
            continue
    if words == '':
        print("No match found!")
    else:
        print(words)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the Game Hangman!")
    print("I am thinking of a word which is", len(secret_word), 'long')
    print("--------------------")
    Guesses = 6
    Warnings = 3
    letters_guessed = []
    vowels = ['a','e','i','u','o']
    while Guesses > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        print("You have", Warnings, 'Warnings left.')
        print("You have", Guesses, 'guesses left.')
        print("Available Letters:", get_available_letters(letters_guessed))
        guess = input('Please guess a letter:')
        guess = guess.strip().lower()
        if guess == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))

        elif guess in secret_word:
            if guess in letters_guessed:
                if Warnings > 0:
                    Warnings -= 1
                    print("Oops! You have already guessed that letter. You now have", Warnings, "Warnings left"
                                                                                                "\n Word: ",
                          get_guessed_word(secret_word, letters_guessed))
                else:
                    Guesses -= 1
                    print("Oops! You have already guessed that letter. Word:",
                          get_guessed_word(secret_word, letters_guessed))
            elif guess not in letters_guessed:
                letters_guessed.append(guess)
                print('Good Guess!', get_guessed_word(secret_word, letters_guessed))
        elif guess.isalpha() == False or len(guess) != 1:
            if Warnings > 0:
                Warnings -= 1
                print("Oops! That is not a valid letter. You have", Warnings, "Warnings left.\n Word:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                Guesses -= 1
                print("Oops! That is not a valid letter. Word:",
                      get_guessed_word(secret_word, letters_guessed))
        elif guess in vowels:
            for vowel in vowels:
                if vowel not in secret_word:
                    Guesses -= 2
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            Guesses -= 1
        print("--------------------")
    if is_word_guessed(secret_word, letters_guessed) == True:
        print("Congratulations, You Won!")
        print("Your Score is", Guesses * len(secret_word))
    elif is_word_guessed(secret_word, letters_guessed) == False:
        print("Sorry! you ran out of guesses. The word was", secret_word)

if __name__ == "__main__":
    
    wordlist = load_words()
    # wordlist = _words()

    # To test part 1, comment out the pass line above and
    # uncomment the following three lines.

    # secret_word = 'apple'
    # letters_guessed = ['a','a','l','r','z']
    # print(get_guessed_word(secret_word, letters_guessed))

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
