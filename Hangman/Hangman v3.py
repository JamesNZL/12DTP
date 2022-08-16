import random
## imports the 'random' module to allow program to randomly select a word from the list of words

wordList = ("history", "rock", "glass", "ground", "cap", "talk", "wilderness", "country",
            "approval", "effect", "ornament", "legs", "ball", "condition", "sky", "hole",
            "sugar", "scent", "loss", "muscle", "ice", "bears", "house", "discovery", "mine",
            "education", "mask", "snow", "twig", "cloth", "interest", "tank", "pets",
            "insurance", "goose", "invention", "haircut", "glove", "straw", "hole", "table",
            "squirrel", "fly", "distance", "brother", "touch", "library", "lunchroom", "produce",
            "stranger", "sand", "cows", "celery", "achiever", "attention", "island", "fang",
            "letter", "debt", "apple", "quilt", "thumb", "aftermath", "stomach", "shade",
            "instrument", "idea", "trip", "stop", "meat", "sleet", "fireman", "trees", "spring",
            "milk", "work", "bite", "oranges", "key", "stick", "stop", "basin", "boat", "quarter",
            "vest", "operation", "brain", "table", "doll", "position", "downtown", "goldfish",
            "ladybug", "quilt", "throat", "friction", "bat", "circle", "boys", "silk")
## create a tuple that contains a list of all the words that could be selected

def clear():
## creates a function called 'clear' that resets iterative variables to the starting values for if the user wants to play again
    global numRounds, numGames, game, restart
    ## allows for modifications to specified variables to be made globally rather than just within the function
    
    numRounds = ""
    numGames = ""
    game = 1
    restart = ""
    ## clears the iterative functions (i.e. if these are not cleared, the program will not function correctly if the user plays again through the built in feature)

def userSelection(variable, maximum, printMessage, inputMessage, variablePrint):
## creates a function called 'userSelection' with arguments that allow it to serve as both an input for number of games and number of rounds
    while variable not in range(1, maximum + 1):
    ## while the user input is outside the range of valid inputs (upper value is maximum + 1 as the range function does not run the specified value):
    ## i.e. range(1, 5) will run 1, 2, 3, and 4, therefore the maximum + 1 ensures the maximum value is inclusive, not exclusive
        try:
        ## try the following:
            print(printMessage)
            ## prints a message that is specified when function is executed
            variable = int(input(inputMessage))
            ## stores the user's input as an integer under the variable name which is specified when function is executed
            
            if variable < 1:
            ## if the user's input is too low (less than the minimum of 1):
                print("\nThe minimum number of {} is 1.".format(variablePrint))
                ## remind the user the minimum is 1
                
            elif variable > maximum:
            ## if the user's input is too high (greater than the specified maximum):
                print("\nThe maximum number of {} is {}.".format(variablePrint, str(maximum)))
                ## remind the user what the specified maximum value is
                
        except:
        ## if an error occurs (i.e. if the user's input is not an integer):
            print("\nYou must enter an integer between 1 and {}.".format(str(maximum)))
            ## remind the user they must enter an integer within the specified range
            
    return variable
    ## when the user's input is valid, return the value of the user's input

def hangman():
## creates a function called 'hangman' which is the main code of the program (i.e. is the 'hangman' part of the program)
    global game
    ## allows for the modifications to the variable 'game' to be made globally rather than just within the function
    
    word = random.choice(wordList)
    ## selects a random word from the list of words and stores it under the 'word' variable
    correctGuesses = []
    wrongGuesses = []
    ## clears the specified lists each time a new word is selected
    count = 0
    ## sets the number of incorrect guesses back to 0 each time a new word is selected
    printWord = list("_" * len(word))
    ## sets the 'printWord' variable as a list which contains the same amount of _ characters as the number of letters in the selected word
    ## this is done as a list to allow for a specific _ to be replaced when a correct letter is guessed (item assignment)

    print("\nWelcome to game number {}!".format(game))
    ## print a message telling the user what number game this is

    while count < numRounds and printWord != list(word):
    ## while the user still has guesses left, and has not yet correctly guessed the word:
        print("\n{}".format(" ".join(printWord)))
        ## converts the 'printWord' list to a string with spaces between each _ and prints it out to the user

        if count > 0:
        ## if 'count' is greater than 0 (i.e. don't run on the first guess):
            print("\nWrong guesses: {}".format(" ".join(wrongGuesses)))
            ## print the user's incorrect guesses out to them

        if numRounds - count == 1:
        ## if the user only has one guess left:
            print("\nYou have 1 incorrect guess left.")
            ## tell the user they only have one guess left
            ## this is done seperately from the print below for correct grammar (i.e. instead of 'guess(es)')

        else:
        ## if the user has more than one guess left (as numRounds - count will never be less than 1):
            print("\nYou have {} incorrect guesses left.".format(numRounds - count))
            ## tell the user how many incorrect guesses they have left

        userInput = list(input("\nInput your guess: "))
        ## stores the user's guess as a list under the variable 'userInput'
        ## this is done as a list as it allows for the user to input multiple letters at once without causing errors, and has exactly the same result as entering them individually
        ## i.e. allows the user to input a full word faster than entering it letter by letter

        for value in userInput:
            ## for each individual letter in the 'userInput' list:
            if value.lower() not in correctGuesses and value.lower() in word:
            ## if the lowercase letter is not already in the 'correctGuesses' list and the letter is in the selected word:
                correctGuesses.append(value.lower())
                ## add the letter to the 'correctGuesses' list as a lowercase letter

            if value.lower() not in wrongGuesses and value.lower() not in word:
            ## if the lowercase letter is not already in the 'wrongGuesses' list and the letter is not in the selected word:
                wrongGuesses.append(value.lower())
                ## add the letter to the 'wrongGuesses' list as a lowercase letter
                count += 1
                ## increase the iterative 'count' variable tracking the user's number of incorrect guesses by 1
                ## this is done as a variable instead of len(wrongGuesses) to help with clarity and ease of understanding

        for letter in range(0, len(word)):
        ## for each letter in the selected word:
            for guess in correctGuesses:
            ## for each correctGuess:
                if guess == word[letter] and printWord[letter] == "_":
                ## if the current correct guess being run is equal the the letter in the selected word currently being run and the corresponding index in 'printWord' has not yet been changed:
                    printWord[letter] = guess
                    ## change the 'printWord' value at the index where the guess equals the letter in the selected word to the correct guess
                    
    if printWord == list(word) and len(wrongGuesses) <= numRounds:
    ## if the 'printWord' list is equal to the selected word (in list form) and the user has less incorrect guesses than they allowed themselves:
    ## second half is required as it prevents the user from entering every letter in one input and 'correctly' guessing the word, as the user's input is stored as a list that is run though entirely
        print("\nCongratulations, you guessed {} correctly!".format(word))
        ## print a congratulatory message telling the user they guessed the word correctly, and what the word was
        
    else:
    ## if the user didn't correctly guess the word:
        print("\nWrong guesses: {}".format(" ".join(wrongGuesses)))
        ## tell the user their final list of incorrect guesses
        print("\nThe word was {}!".format(word))
        ## tell the user the word

    game += 1
    ## increase the iterative 'game' variable tracking the number of games played by 1

clear()
## execute the 'clear' function to clear the iterative variables before the 'hangman' function starts

print("Welcome to Hangman!")
## print a welcome message to the user

while restart != 2:
## while restart is not 2 (2 is the option to end the game):
    clear()
    ## execute the 'clear' function to clear the iterative variables before the 'hangman' function restarts

    numGames = userSelection(numGames, 5, "\nPlease enter the number of games you would like to play.\n\n1) 1 game\n2) 2 games\n3) 3 games\n4) 4 games\n5) 5 games", "\nYour selection: ", "games")
    numRounds = userSelection(numRounds, 15, "\nPlease enter the number of incorrect guesses you would like per word.\n\nPlease note the minimum of 1 guess and the maximum of 15 guesses.", "\nNumber of guesses: ", "guesses")
    ## execute the userSelection' with arguments for both number of games and number of rounds, and store the returned user input under the specified variables

    while game <= numGames:
    ## while the number of games played is less than the selected number of games:
        hangman()
        ## execute the 'hangman' function

    print("\nWould you like to play again?\n\n1) Yes\n2) No")
    ## print a message asking if the user would like to play again, with 1 for yes and 2 for no

    while restart not in range(1, 2 + 1):
    ## while the user input is outside the range of valid inputs (upper value is 2 + 1 as the range function does not run the specified value):
    ## i.e. range(1, 5) will run 1, 2, 3, and 4, therefore the 2 + 1 ensures the 2 is inclusive, not exclusive
        try:
        ## try the following:
            restart = int(input("\nEnter your choice: "))
            ## stores the user's input as an integer under the variable name 'restart'
            if restart not in range(1, 2 + 1):
            ## if the user's input is outside the range of valid inputs:
                print("\nYou must enter either 1 or 2.")
                ## tell the user they must enter either 1 or 2

        except:
        ## if an error occurs (i.e. user's input is not an integer):
            print("\nYou must enter either 1 or 2.")
            ## tell the user they must enter either 1 or 2
print("\nThank you for playing Hangman!")
## prints an exit message to the user
