import sys

regularPizza = 8.5
gourmetPizza = 13.5
pizzaMenu = {"Cheese" : regularPizza,
             "Pepperoni" : regularPizza,
             "Hawaiian" : regularPizza,
             "Ham & Cheese" : regularPizza,
             "BBQ Pork & Onion" : regularPizza,
             "Beef & Onion" : regularPizza,
             "Cheesy Garlic" : regularPizza,
             "Sweet & Sour Chicken" : gourmetPizza,
             "Mega Meatlovers" : gourmetPizza,
             "Garlic Prawn" : gourmetPizza,
             "BBQ Chicken & Rasher Bacon" : gourmetPizza,
             "Butter Chicken" : gourmetPizza
             }
dashedLine = "----------------------------------------------------------------"

def userInput(rangeMaximum, inputMessage, ifError, exceptError):
    inputValue = ""
    while not isinstance(inputValue, int) or inputValue not in range(1, rangeMaximum + 1):
        inputValue = input(inputMessage)
        try:
            inputValue = int(inputValue)
            if inputValue not in range(1, rangeMaximum + 1):
                print(ifError)
        except:
            cancelOrder(inputValue)
            print(exceptError)
    return inputValue

def cancelOrder(checkInput):
    if checkInput.lower() == "x":
        restartOrExit()

def restartOrExit():
    print("\nWould you like to enter another order, or exit the program?\n\n1) Enter another order\n2) Exit program")
    restartInput = userInput(2, "\nEnter your choice: ", "\nYour choice must be either 1 or 2.", "\nYour choice must be an integer that is either 1 or 2.")
    if restartInput == 1:
        orderFunction()
    elif restartInput == 2:
        sys.exit()

def customerInformation(pickupOrDelivery):
    customerAddress = None
    customerNumber = None
    orderCost = 0
    customerName = input("\nInput the customer's name: ")
    cancelOrder(customerName)
    if pickupOrDelivery == 2:
        orderCost += 3
        customerAddress = input("\nInput the customer's address: ")
        cancelOrder(customerAddress)
        while not isinstance(customerNumber, int):
            customerNumber = input("\nInput the customer's phone number: ")
            try:
                customerNumber = int(customerNumber)
            except:
                cancelOrder(customerNumber)
                print("\nThe customer's phone number must not contain any letters, symbols or spaces.")
    return customerName, customerAddress, customerNumber, orderCost

def orderFunction():
    customerOrdered = []
    print("\nIs the order for pick-up or delivery?\n\n1) Pick-up\n2) Delivery")
    pickupOrDelivery = userInput(2, "\nEnter your selection: ", "\nYour selection must be either 1 or 2.", "\nYour selection must be an integer that is either 1 or 2.")
    customerName, customerAddress, customerNumber, orderCost = customerInformation(pickupOrDelivery)
    print("\nHow many pizzas are to be ordered?\n\n1) 1 pizza\n2) 2 pizzas\n3) 3 pizzas\n4) 4 pizzas\n5) 5 pizzas")
    numberOfPizzas = userInput(5, "\nNumber of pizzas: ", "\nThe number of pizzas must be between 1 and 5.", "\nThe number of pizzas must be an integer between 1 and 5.")
    print("\nWhich pizzas would the customer like to order?\n")
    for menuNumber, pizzaName in enumerate(pizzaMenu, 1):
        print("{}) {}".format(menuNumber, pizzaName))
    for orderNumber in range(0, numberOfPizzas):
        customerOrdered.append(userInput(len(pizzaMenu), "\nEnter the corresponding number: ", "\nYour input must be between 1 and {}.".format(len(pizzaMenu)), "\nYour input must be an integer between 1 and {}.".format(len(pizzaMenu))))
    for orderedIndex in range(0, len(customerOrdered)):
        for menuNumber, pizzaName in enumerate(pizzaMenu, 1):
            if customerOrdered[orderedIndex] == menuNumber:
                customerOrdered[orderedIndex] = pizzaName
    print("\n{}\n".format(dashedLine))
    for pizzaNumber, pizzaName in enumerate(customerOrdered, 1):
        print("{}) {} – ${}".format(pizzaNumber, pizzaName, pizzaMenu[pizzaName]))
        orderCost += pizzaMenu[pizzaName]
    print("\nTotal cost of order: ${}".format(orderCost))
    print("\nCustomer's name: {}".format(customerName))
    if pickupOrDelivery == 2:
        print("\nCustomer's address: {}".format(customerAddress))
        print("\nCustomer's phone number: {}".format(customerNumber))
    print("\n{}".format(dashedLine))
    restartOrExit()

print("If you would like to cancel the order at any time, enter 'x' (case insensitive).")
orderFunction()
