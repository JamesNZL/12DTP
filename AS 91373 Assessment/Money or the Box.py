import random
## imports random module to increase capabilities

prizes = ["a car", "an overseas holiday", "a TV", "a box of chocolates", "a DVD"]
## creates a list containing all the prizes
## this is a list to allow for it to be shuffled, and as it allows for it to be modified later
random.shuffle(prizes)
## shuffles the prizes around in the list randomly
selectedBox = ""
alreadyOffered = 0
cashOrBox = ""
## initialises these values at the beginning to prevent 'referenced before assignment' errors in conditional statements

def offerGenerator(offerMin, offerMax, offerStep):
## creates a function that generates a random number between the specified min and max values in specified increments
    return random.randrange(offerMin, offerMax + offerStep, offerStep)
    ## randomly generates a number between offerMin and offerMax, in increments of offerStep
    ## the upper value is offerMax + offerStep as the upper boundary is exclusive
    ## returns the randomly generated value

def userInput(rangeMaximum, inputMessage, ifError, exceptError):
## creates a function for player input with validity checks which are specified for the specific intended input
## this is a function to prevent repetition of the majority of the code
    inputValue = ""
    ## initialises/replaces inputValue to prevent 'referenced before assignment' error and to clear any previous inputs

    while not isinstance(inputValue, int) or inputValue not in range(1, rangeMaximum + 1):
    ## while the userInput is not a valid input (not an integer, and not in the valid range):
        try:
        ## try to:
            inputValue = int(input(inputMessage))
            ## set inputValue to be the player's input with a data type of integer
            if inputValue not in range(1, rangeMaximum + 1):
            ## if the inputValue is an integer but is outside of the valid range:
                print(ifError)
                ## print the specified error message for this error situation

        except:
        ## if the player's input is not able to be converted to an integer:
            print(exceptError)
            ## print the specified error message for this error situation

    return inputValue
    ## returns the player's input

print("Welcome to 'Money or the Box'!")
## prints a welcome message
print("\nPlease select one of the following prizes:\n")
## prints an input prompt for the box number the player wishes to select

for boxNumber in range(1, len(prizes) + 1):
## assigns a number to each prize in the shuffled order and for each do:
## the upper value for the range is len(prizes) + 1 as the upper boundary is exclusive
    print("{}) Box #{}".format(boxNumber, boxNumber))
    ## print x) Box #x for each prize

selectedBox = userInput(len(prizes), "\nEnter your selection: ", "\nYour selection must be between 1 and {}.".format(len(prizes)), "\nYour selection must be an integer between 1 and {}.".format(len(prizes)))
## gets the player's input for their selected box through the userInput function with the appropriate values and messages

numberOfOffers = random.randint(1, 5)
## generates a random number between 1 and 5 for how many times the code should offer the player a cash amount

while alreadyOffered < numberOfOffers and cashOrBox != 1:
## while the number of cash offers is less than the randomly generated amount and the player hasn't accepted the cash:
    if alreadyOffered == 0:
    ## if this is the first offer:
        currentOffer = offerGenerator(200, 500, 50)
        ## set the iterative variable tracking the cash offer to a randomly generated number between 200 and 500 in increments of 50

    else:
    ## if there has already been a cash offer:
        currentOffer += offerGenerator(200, 5000, 100)
        ## generate a new random number between 200 and 5000 in increments of 100 and add it to the previous offer

    print("\nWould you like to take the offer of ${}, or keep the box?\n\n1) Give me the cash!\n2) I want the box!".format(currentOffer))
    ## print an input prompt for whether the user wishes to keep the box or take the cash offer

    cashOrBox = userInput(2, "\nEnter your choice: ", "\nYour choice must be either a 1 or 2.", "\nYour choice must be an integer that is either 1 or 2.")
    ## gets the player's input for their selected choice through the userInput function with the appropriate values and messages

    alreadyOffered += 1
    ## add to the iterative variable tracking the number of cash offers given by 1   

if cashOrBox == 1:
## if the player has chosen the cash offer:
    print("\nYou have been given ${}, you have missed out on {}.".format(currentOffer, prizes[selectedBox - 1]))
    ## tell the user how much money they have been given, and what was in the box
    
else:
## if the player chose to keep the box:
    print("\nCongratulations! You have won {}!".format(prizes[selectedBox - 1]))
    ## tell the user what they have won

print("\nThank you for playing 'Money or the Box'! Hope to see you again soon!")
## prints an exit message to the user
