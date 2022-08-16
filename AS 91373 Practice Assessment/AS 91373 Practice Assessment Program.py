## imports the sys function to allow me to exit the program via sys.exit()
import sys

## creates a function for integer inputs with validity checking named user_input with the parameters rangeMaximum and promptWord
## rangeMaximum is the inclusive upper boundary of the permitted range
## promptWord a word/phrase specific to the input (e.g. 'choice' or 'selection')
def user_input(rangeMaximum, promptWord):
    ## clears the inputValue each time the function is run
    inputValue = ""

    ## while the inputValue isn't in the permitted range, do:
    ## RANGE_OFFSET is compensation for the fact that the specified upper boundary in a range is exclusive
    while inputValue not in range(MINIMUM_INPUT, rangeMaximum + RANGE_OFFSET):
        ## tries to do the following:
        try:
            ## sets inputValue to the user's input in an integer form
            inputValue = int(input("\nEnter {}: ".format(promptWord)))

            ## if the inputValue is an integer but not in the permitted range:
            if inputValue not in range(MINIMUM_INPUT, rangeMaximum + RANGE_OFFSET):
                ## prints an error message stating the input must be in the permitted range
                print("\n{} must be between {} and {}.".format(promptWord.capitalize(), MINIMUM_INPUT, rangeMaximum))

        ## if the user's input cannot be stored as an integer, or another error occurs:
        except:
            ## prints an error message stating the input must be an integer in the permitted range
            print("\n{} must be an integer between {} and {}.".format(promptWord.capitalize(), MINIMUM_INPUT, rangeMaximum))

    ## returns the user's input once valid
    return inputValue

## creates a function for outputting a list/tuple in a numbered list named numbered_output with the parameter dataStructure
## dataStructure stores the list/tuple to be printed
def numbered_output(dataStructure):
    ## for each item's numbered position and value in the numbered dataStructure, do:
    for number, item in enumerate(dataStructure, ENUMERATE_START):
        ## print the numbered position and the item's value
        print("{}) {}".format(number, item))

## creates a function for if the order is cancelled/completed which determines whether to enter another order or exit named restart_or_exit
## this is a seperate function to allow for only restart/exit to be run
def restart_or_exit():
    ## creates a tuple called ACTION_OPTIONS which stores the options for when the order is completed or cancelled
    ## this is a tuple for in the unlikely event that options need to be edited or added/removed
    ACTION_OPTIONS = ("Enter another order", "Exit program")
    ## prints a prompt asking the user whether they would like to enter another order or exit
    print("\nWould you like to enter another order, or exit the program?\n")
    ## calls the numbered_output function with the ACTION_OPTIONS tuple
    numbered_output(ACTION_OPTIONS)
    ## calls the user_input function with the upper boundary as the length of ACTION_OPTIONS and 'your choice' as the promptWord
    ## the returned value is then stored within restartInput
    restartInput = user_input(len(ACTION_OPTIONS), "your choice")

    ## if the user wants to exit the program:
    ## INDEX_OFFSET is compensation for the fact that indexing begins at 0, while the numbered output for the user's input begins at 1
    if ACTION_OPTIONS[restartInput - INDEX_OFFSET] == "Exit program":
        ## exits the program
        sys.exit()

## creates a function which collects the customer's information called customer_information with the parameter pickupOrDelivery
## pickupOrDelivery stores whether the current order is pick-up or delivery, and therefore whether address/phone number is required
def customer_information(pickupOrDelivery):
    ## initialises/clears the following variables
    customerName = ""
    customerAddress = None
    customerNumber = None
    orderCost = 0

    ## while the customer's name contains any invalid characters (not in A-Z):
    while not customerName.isalpha():
        ## prompts input for the customer's first name
        customerName = input("\nInput the customer's first name: ")

        ## if the customer's first name is not fully A-Z:
        if not customerName.isalpha():
            ## prints an error message stating the name must not contain any invalid characters (not in A-Z)
            print("\nThe customer's first name must only contain letters A-Z.")

    ## if the current order is for delivery:
    if pickupOrDelivery == "Delivery":
        ## add the DELIVERY_COST to the total cost
        orderCost += DELIVERY_COST

        ## prompts input for the customer's address
        customerAddress = input("\nInput the customer's address: ")

        ## while the customer's number isn't an integer / can't be stored as an integer:
        ## user_input is not called here as the phone number doesn't have a range it must fit within
        ## therefore, the only validity checking required is that the phone number doesn't contain letters or symbols
        while not isinstance(customerNumber, int)
            ## tries the following:
            try:
                ## prompts input for the customer's phone number and attempts to store as an integer
                customerNumber = int(input("\nInput the customer's phone number: "))

            ## if the customer's phone number contains letters or symbols or another error occurs:
            except:
                ## prints an error message stating that the customer's phone number must not contain any non-number characters
                print("\nThe customer's phone number must not contain any letters, symbols or spaces.")

    ## returns the customer's name, address, phone number and current total cost
    return customerName, customerAddress, customerNumber, orderCost

## initialises the following constants
DASHED_LINE = 72
REGULAR_PIZZA = 8.5
GOURMET_PIZZA = 13.5
DELIVERY_COST = 3
MINIMUM_INPUT = 1
RANGE_OFFSET = 1
INDEX_OFFSET = 1
INDEX_START = 0
ENUMERATE_START = 1
PIZZA_MENU = {"Cheese":REGULAR_PIZZA,
              "Pepperoni":REGULAR_PIZZA,
              "Hawaiian":REGULAR_PIZZA,
              "Ham & Cheese":REGULAR_PIZZA,
              "BBQ Pork & Onion":REGULAR_PIZZA,
              "Beef & Onion":REGULAR_PIZZA,
              "Cheesy Garlic":REGULAR_PIZZA,
              "Sweet & Sour Chicken":GOURMET_PIZZA,
              "Mega Meatlovers":GOURMET_PIZZA,
              "Garlic Prawn":GOURMET_PIZZA,
              "BBQ Chicken & Rasher Bacon":GOURMET_PIZZA,
              "Butter Chicken":GOURMET_PIZZA,
              }

## prints a welcome message to the employee
print("Welcome to Dream Pizzas' new order input system!")

## do the following forever, until the program is quit:
while True:
    ## initialises/clears the customerOrdered list which stores the current ordered pizzas
    customerOrdered = []

    ## creates a tuple called OBTAINING_OPTIONS which stores the options for how the order is recieved
    ## again, this is a tuple for in the unlikely event that options need to be edited or added/removed
    OBTAINING_OPTIONS = ("Pick-up", "Delivery")
    ## prints a prompt asking whether the order is for pick-up or delivery
    print("\nIs the order for pick-up or delivery?\n")
    ## calls the numbered_output function with the OBTAINING_OPTIONS tuple
    numbered_output(OBTAINING_OPTIONS)
    ## calls the user_input function with the upper boundary as the length of OBTAINING_OPTIONS and 'your selection' as the promptWord
    ## the returned value is then stored within pickupOrDelivery
    pickupOrDelivery = user_input(len(OBTAINING_OPTIONS), "your selection")

    ## calls the customer_information function with pickupOrDelivery set to the user's selectied value within OBTAINING_OPTIONS
    ## again, INDEX_OFFSET is compensation for indexing beginning at 0 while the prompt beginning at 1
    customerName, customerAddress, customerNumber, orderCost = customer_information(OBTAINING_OPTIONS[pickupOrDelivery - INDEX_OFFSET])

    ## creates a tuple called QUANTITY_OPTIONS which stores the options for how many pizzas may be ordered
    ## then goes through the the exact same process as for ACTION_OPTIONS and OBTAINING_OPTIONS
    QUANTITY_OPTIONS = ("1 pizza", "2 pizzas", "3 pizzas", "4 pizzas", "5 pizzas")
    print("\nHow many pizzas are to be ordered?\n")
    numbered_output(QUANTITY_OPTIONS)
    numberOfPizzas = user_input(len(QUANTITY_OPTIONS), "the number of pizzas")

    ## prints a prompt asking which pizzas from the menu the customer wants to order
    print("\nWhich pizzas would the customer like to order?\n")
    ## calls the numbered_output function with the PIZZA_MENU dictionary
    ## this is fine although a dictionary would have three data positions (enumerate value, key, value)
    ## compared to the two of a tuple (enumerate value, value) as I am not using the data in the value position of the dictionary
    numbered_output(PIZZA_MENU)

    ## repeats the following code the exact number of times for the number of pizzas the customer wants to order
    for orderNumber in range(INDEX_START, numberOfPizzas):
        ## calls the user_input function with the upper boundary as the length of the menu and 'the corresponding number' as the promptWord
        ## the returned value is then appended to the end of customerOrdered
        customerOrdered.append(user_input(len(PIZZA_MENU), "the corresponding number"))

    ## for each ordered pizza in the customerOrdered list:
    for orderedIndex in range(INDEX_START, len(customerOrdered)):
        ## for each location on the menu and the pizza at that location within the numbered PIZZA_MENU:
        for menuNumber, pizzaName in enumerate(PIZZA_MENU, ENUMERATE_START):
            ## if the menu number of the ordered pizza is the same as the menu number currently being iterated:
            if customerOrdered[orderedIndex] == menuNumber:
                ## replaces the current value within customerOrdered to the name of the pizza (e.g. 1 is changed to 'Cheese')
                customerOrdered[orderedIndex] = pizzaName

    ## as with the three previous ..._OPTIONS
    CONFIRM_OPTIONS = ("Confirm order", "Cancel order")
    print("\nWould you like to confirm the order, or cancel the order?\n")
    numbered_output(CONFIRM_OPTIONS)
    confirmOrCancel = user_input(len(CONFIRM_OPTIONS), "your choice")

    ## if the user wants to cancel the order:
    if CONFIRM_OPTIONS[confirmOrCancel - INDEX_OFFSET] == "Cancel order":
        ## calls the restart_or_exit function
        restart_or_exit()
        ## if the program hasn't been force quit (i.e. if the user wishes to restart this/another order):
        ## restarts this top-level while loop
        continue

    ## prints a seperation banner
    print("\n{}\n".format("-" * DASHED_LINE))

    ## for each pizza number and pizza name in the numbered customerOrdered list:
    for pizzaNumber, pizzaName in enumerate(customerOrdered, ENUMERATE_START):
        ## prints the pizza number, pizza name and the price of the pizza to the employee
        print("{}) {} – ${}0".format(pizzaNumber, pizzaName, PIZZA_MENU[pizzaName]))
        ## adds the individual cost of the pizza to the total order cost
        orderCost += PIZZA_MENU[pizzaName]

    ## prints the total cost of the order
    print("\nTotal cost of order: ${}0".format(orderCost))
    ## prints the customer's first name
    print("\nCustomer's name: {}".format(customerName))

    ## if the order is for delivery:
    if OBTAINING_OPTIONS[pickupOrDelivery - INDEX_OFFSET] == "Delivery":
        ## prints the customer's address
        print("\nCustomer's address: {}".format(customerAddress))
        ## prints the customer's phone number
        print("\nCustomer's phone number: {}".format(customerNumber))

    ## prints another seperation banner
    print("\n{}".format("-" * DASHED_LINE))

    ## calls restart_or_exit
    restart_or_exit()
