import sys                                                                                                                                                                                          ##
import time                                                                                                                                                                                         ## imports modules to enable extra capabilities

validEthnicities = ["NZ European", "Pasifika", "Maori", "Asian", "Indian"]                                                                                                                          ##                                                                                                                                                                        ##
ethEuro = [18.5, 18.5, 25, 30]                                                                                                                                                                      ##
ethMaori = [18.5, 18.5, 26, 32]                                                                                                                                                                     ## sets declared variable names to contain the
ethAsian = [18.5, 18.5, 23, 25]                                                                                                                                                                     ## declared strings and values and store then as a list

userValidity = "0"                                                                                                                                                                                  ## 
userEthnicity = "0"                                                                                                                                                                                 ##
inputEthnicity = "0"
userBMI = 0.0                                                                                                                                                                                       ##
userWeight = 0.0                                                                                                                                                                                    ##
userHeight = 0.0                                                                                                                                                                                    ## sets declared variable names 
sleepTime = 0                                                                                                                                                                                ## to contain the declared values

print("Welcome to the New Zealand BMI Calculator v1!\n")                                                                                                                                            ## prints a welcome message to the screen
time.sleep(sleepTime)                                                                                                                                                                               ## pauses for sleepTime seconds*

while userValidity not in ["1", "2"]:                                                                                                                                                            ## while the user input is not 'Yes' or 'No', do:
    print("Are you under 18, shorter than 1.5m, taller than 1.9m, an athlete or bodybuilder, currently pregnant or breastfeeding?\n\n1) Yes\n2) No")                                                ##     ensures the user meets all appropriate critera
    userValidity = input("\nEnter your choice: ")

    if userValidity == "1":                                                                                                                                                                       ##     if they are ineligible, do:
        print("\nUnfortunately you are currently ineligible for this BMI calculator, sorry!")                                                                                                         ##         prints a message informing the user they are ineligible
        time.sleep(sleepTime)                                                                                                                                                                       ##         pauses for sleepTime
        sys.exit()                                                                                                                                                                                  ##         kills the program

    elif userValidity not in ["1", "2"]:                                                                                                                                                         ##     if the user enters something that is not 'Yes' or 'No', do:
        print("You must enter either '1' or '2'.\n")                                                                                                  ##         prints an error message detailing the valid responses
        time.sleep(sleepTime)                                                                                                                                                                       ##         pauses for sleepTime

while inputEthnicity not in ["1", "2", "3", "4", "5"]:                                                                                                                                                        ## while the user input is not a valid ethnicity, 
    print("\nWhat ethnicity are you?\n\n1) NZ European\n2) Pasifika\n3) Maori\n4) Asian\n5) Indian")
    inputEthnicity = input("\nPlease enter your ethnicity: ")                                                                                                                                       ##     asks the user to enter their ethnicity

    if inputEthnicity not in ["1", "2", "3", "4", "5"]:                                                                                                                                                       ##     if the user enters an invalid ethnicity, do:
        print("You must enter either '1', '2', '3', '4' or '5'.") ##         prints an error message detailing the valid ethnicities
        time.sleep(sleepTime)                                                                                                                                                                       ##         pauses for sleepTime

    userEthnicity = validEthnicities[(int(inputEthnicity) - 1)]

def userInput(userVar, minValue, maxValue, varName, varUnit):                                                                                                                                       ## creates the userInput function, with declared placeholders

    global userWeight                                                                                                                                                                               ## 
    global userHeight                                                                                                                                                                               ##     sets the declared variables to global variables

    while userVar < minValue or userVar > maxValue:                                                                                                                                                 ##     while weight/height is too low or too high, do:
        userVar = float(input("\nPlease enter your " + varName + " in " + varUnit + ".\n"))                                                                                                         ##         asks the user to input their weight/height

        if userVar < minValue:                                                                                                                                                                      ##         if weight/height is too low, do:
            print("The minimum " + varName + " is " + str(minValue) + " " + varUnit + ".")                                                                                                          ##              prints an error message detailing the min weight/height
            time.sleep(sleepTime)                                                                                                                                                                   ##              pauses for sleepTime

        elif userVar > maxValue:                                                                                                                                                                    ##         if weight/height is too high, do:
            print("The maximum " + varName + " is " + str(maxValue) + " " + varUnit + ".")                                                                                                          ##              prints an error message detailing the max weight/height
            time.sleep(sleepTime)                                                                                                                                                                   ##              pauses for sleepTime

        if varName == "weight":                                                                                                                                                                     ##         if current input is for weight, do:
            userWeight = userVar                                                                                                                                                                    ##              sets userWeight variable to user's input

        else:                                                                                                                                                                                       ##         if current input is for height, do:
            userHeight = userVar                                                                                                                                                                    ##              sets userHeight variable to user's input

userInput(userWeight, 40.0, 160.0, "weight", "kilograms")                                                                                                                                           ## runs the userInput function with declared arguments for weight
userInput(userHeight, 1.5, 1.9, "height", "metres")                                                                                                                                                 ## runs the userInput function with declared arguments for height

def printOut(weightClass, diseaseRisk):                                                                                                                                                             ## creates the printOut function, with declared placeholders
    print("You are classed as " + weightClass + " with a BMI score of " + str(userBMI) + ".")                                                                                                       ##     prints user's weight class and BMI score
    time.sleep(sleepTime)                                                                                                                                                                           ##     pauses for sleepTime
    print("\nThis places you at a " + diseaseRisk + " risk of obesity related diseases.")                                                                                                           ##     prints user's risk of obesity-related diseases
    time.sleep(sleepTime)                                                                                                                                                                           ##     pauses for sleepTime
    print("\nPlease note that your Body Mass Index (BMI) is only a general indication of health, and you should consult your doctor with any concerns.")                                            ##     prints a disclaimer that BMI is only a general indication, etc.

def calc(userEth):                                                                                                                                                                                  ## creates the calc function, with declared placeholders

    global userBMI                                                                                                                                                                                  ##     sets userBMI variable to global variable

    userBMI = float(round(userWeight/userHeight**2,1))                                                                                                                                              ##     calculates user's BMI to 1 d.p. with user's weight and height
    
    if userBMI < userEth[0]:                                                                                                                                                                        ##     if userBMI is classed as underweight, do:
        printOut("underweight", "low")                                                                                                                                                              ##         runs the printOut function with strings for underweight

    elif userBMI >= userEth[1] and userBMI < userEth[2]:                                                                                                                                            ##     if userBMI is classed as a healthy weight, do:
        printOut("a healthy weight", "normal")                                                                                                                                                      ##         runs the printOut function with strings for a healthy weight

    elif userBMI >= userEth[2] and userBMI < userEth[3]:                                                                                                                                            ##     if userBMI is classed as overweight, do:
        printOut("overweight", "high")                                                                                                                                                              ##         runs the printOut function with strings for overweight

    elif userBMI >= userEth[3]:                                                                                                                                                                     ##     if userBMI is classed as obese, do:
        printOut("obese", "very high")                                                                                                                                                              ##         runs the printOut function with strings for obese

if userEthnicity == validEthnicities[0]:                                                                                                                                                            ## if the user is NZ European, do:
    calc(ethEuro)                                                                                                                                                                                   ##     runs the calc function with BMI groups for NZ Europeans
    
elif userEthnicity == validEthnicities[1] or userEthnicity == validEthnicities[2]:                                                                                                                  ## if the user is Pasifika or Māori, do:
    calc(ethMaori)                                                                                                                                                                                  ##     runs the calc function with BMI groups for Pacific Island & Māori
    
elif userEthnicity == validEthnicities[3] or userEthnicity == validEthnicities[4]:                                                                                                                  ## if the user is Asian or Indian, do:
    calc(ethAsian)                                                                                                                                                                                  ##     runs the calc function with BMI groups for Asian & Indian

                                                                                                                                                                                                    ## *viz. 0.75s to make reading easier
