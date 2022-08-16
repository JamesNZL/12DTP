import time

sleepTime = 0
userSubjects = []
userStandards = []
userCredits = [0, 0, 0, 0]
nceaLevels = (1, 2, 3)
requiredCredits = (80, 60)
endorsementCredits = 50
##markLevels = ("Not Achieved", "Achieved", "Merit", "Excellence")
validMarks = ("NA", "A", "M", "E")
yesNo = ("Yes", "No")

def sleepMessage(message):
    time.sleep(sleepTime)
    print(message)
    time.sleep(sleepTime)

def userInformation():

    global userLevel
    global previousPass

    userLevel = ""
    inputPassed = ""
    previousPass = False

    while userLevel not in nceaLevels:
        userLevel = input("Please enter the NCEA Level you are currently studying. (1 to 3)\n")

        try:
            userLevel = int(userLevel)

        except:
            sleepMessage("\nYou must enter a number between 1 and 3.\n")

        if userLevel in nceaLevels:
            for level in reversed(range(1, 3)):
                if userLevel > level:
                    while inputPassed.title() not in yesNo:
                        inputPassed = input("\nDid you pass NCEA Level " + str(level) + "? ('Yes' or 'No')\n")

                        if inputPassed.title() not in yesNo:
                            sleepMessage("\nPlease enter either 'Yes' or 'No'.")

                        if inputPassed.title() == yesNo[0]:
                            previousPass = True
            
        if userLevel not in nceaLevels and str(userLevel).isnumeric():
            sleepMessage("\nThe NCEA Level must only consist of numbers 1 to 3.\n")
                
    subjectInput()

def subjectInput():

    time.sleep(sleepTime)

    global userSubjects
    global numberOfSubjects
    inputSubject = ""
    numberOfSubjects = 0

    while inputSubject.lower() != "x" or numberOfSubjects == 0:
        if inputSubject != "" and inputSubject.replace(" ", "").isalpha() and inputSubject.lower() != "x" and inputSubject not in userSubjects:
            userSubjects.append(inputSubject.title())

        print("\nPlease enter the name of one of your subjects. (e.g. 'Maths')")
        sleepMessage("\nIf you have finished entering all your subjects, please enter 'x'.")
        inputSubject = input("\nYou have already entered: '" + "', '".join(userSubjects) + "'\n")

        numberOfSubjects = len(userSubjects)

        if inputSubject.lower() == "x" and numberOfSubjects == 0:
            sleepMessage("\nYou must enter at least one subject.")

        if not inputSubject.replace(" ", "").isalpha():
            sleepMessage("\nThe subject name must only consist of letters A-Z.")

    standardInput()

def standardInput():

    time.sleep(sleepTime)

    global userStandards
    global numberOfStandards
    inputStandard = ""

    for subject in userSubjects:
        numberOfStandards = 0
        newStandards = []

        while inputStandard.lower() != "x" or numberOfStandards == 0:
            if inputStandard != "" and inputStandard.isnumeric() and inputStandard.lower() != "x" and inputStandard not in userStandards:
                newStandards.append(inputStandard)
                userStandards.append(inputStandard)

            print("\nPlease enter one of your standard numbers for " + subject + ". (e.g. '91027')")
            sleepMessage("\nIf you have finished entering all your standard numbers for " + subject + ", please enter 'x'.")
            inputStandard = input("\nYou have already entered: '" + "', '".join(newStandards) + "'\n")

            numberOfStandards = len(newStandards)

            if inputStandard.lower() == "x" and numberOfStandards == 0:
                sleepMessage("\nYou must enter at least one standard number.")

            if inputStandard.lower() != "x" and not inputStandard.isnumeric():
                sleepMessage("\nThe standard number must only consist of numbers 0-9.")

    markInput()

def markInput():

    time.sleep(sleepTime)

    argLength = 2

    for standard in userStandards:
        markValid = False

        while markValid == False:
            print("\nPlease enter your mark and number of credits for Standard " + standard + " seperated by ', '. (e.g. 'E, 4')")
            time.sleep(sleepTime)
            inputMark = input("\nPlease enter your mark as one of the following: '" + validMarks[0] + "', '" + validMarks[1] + "', '" + validMarks[2] + "', or '" + validMarks[3] + "'.\n")

            if ", " in inputMark:
                inputMark = inputMark.split(", ")
                
                if inputMark[0].upper() in validMarks and inputMark[0].isalpha() and inputMark[1].isnumeric() and len(inputMark) == argLength:
                    markValid = True
                    
                    markCalc(inputMark[0], inputMark[1])
                                      
                elif inputMark[0].isnumeric() and inputMark[1].isalpha() and inputMark[1].upper() in validMarks and len(inputMark) == argLength:
                    sleepMessage("\nYou must enter your mark followed by the number of credits, in that order. (e.g. 'E, 4')")
                    
                elif len(inputMark) < argLength:
                    sleepMessage("\nYou must enter both your mark and your number of credits for Standard " + standard + ".")

                elif len(inputMark) > argLength:
                    sleepMessage("\nYou must only enter your mark and number of credits for Standard " + standard + ".")

                elif inputMark[0].upper in validMarks and inputMark[1] in validMarks:
                    sleepMessage("\nYou must enter the number of credits for Standard " + standard + ".")

                elif inputMark[0].upper not in validMarks and inputMark[1].upper not in validMarks:
                    sleepMessage("\nYou must enter your mark for Standard " + standard + ".")

                else:
                    sleepMessage("\nPlease follow the specified layout of '[MARK], [NO. CREDITS]'.")
                    
            else:
                sleepMessage("\nYou must enter your mark and number of credits seperated by ', '.")

    programOutput()

def markCalc(userMark, standardCredits):

    global userCredits

    for mark in range(0, 4):
        if userMark.upper() == validMarks[mark]:
            userCredits[mark] = userCredits[mark] + int(standardCredits)

def programOutput():

    global totalCredits

    totalCredits = userCredits[1] + userCredits[2] + userCredits[3]

    if previousPass == False:
        userPassed(0)

    elif previousPass == True:
        userPassed(1)

    sleepMessage("\nYou have achieved a total of " + str(totalCredits) + " credits, with " + str(userCredits[0]) + " Not Achieved credits, " + str(userCredits[1]) + " Achieved credits, " + str(userCredits[2]) + " Merit credits, and " + str(userCredits[3]) + " Excellence credits.")

def userPassed(creditValue):
    if totalCredits >= requiredCredits[creditValue]:
        if userCredits[3] >= endorsementCredits:
            print("\nCongratulations, you have passed NCEA Level " + str(userLevel) + " with an endorsement at Excellence level!")

        elif userCredits[2] >= endorsementCredits:
            print("\nCongratulations, you have passed NCEA Level " + str(userLevel) + " with an endorsement at Merit level!")
            time.sleep(sleepTime)
            print("\nTo endorse at Excellence level, you must achieve " + str(endorsementCredits - userCredits[3]) + " more Excellence credits.")
        
        else:
            print("\nCongratulations, you have passed NCEA Level " + str(userLevel) + "!")
            sleepMessage("\nTo endorse at Merit level, you must achieve " + str(endorsementCredits - userCredits[2]) + " more Merit credits.")
            print("\nTo endorse at Excellence level, you must achieve " + str(endorsementCredits - userCredits[3]) + " more Excellence credits.")

    else:
        print("\nTo pass NCEA Level " + str(userLevel) + ", you must achieve " + str(requiredCredits[creditValue] - totalCredits) + " more credits.")

userInformation()
