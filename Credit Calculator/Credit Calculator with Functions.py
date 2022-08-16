import sys                                                                                                   ## import the sys module

LEVEL1 = 80                                                                                                  ##
LEVEL2 = 60                                                                                                  ##
LEVEL3 = 60                                                                                                  ## (not necessarily correct, as if you failed the previous year, you must still attain 80 credits at Level 2 or 3)
uniEntrance = 0                                                                                              ## initialise and assign specified values to specified variables

def passLevel1(total):                                                                                       ## create a function with the name passLevel1 and the redundant placeholder 'total' (already a variable, can be referenced within the function w/o being an argument)
    if total >= LEVEL1:                                                                                      ##     if the user has over 80 credits:
        print (name,", You have enough credits to pass level 1 NCEA")                                        ##         tell the user that they have passed Level 1
        return True                                                                                          ##         return a value of True
    else:                                                                                                    ##     if the user has less than 80 credits:
        remaining = (LEVEL1 - total)                                                                         ##         set a variable to the amount of credits the user needs
        print (name,", You need {} more credits to pass level 1 NCEA".format(remaining))                     ##         tell the user how many credits they still need

def passLevel2(total):                                                                                       ## 
    if total >= LEVEL2:                                                                                      ##
        print (name,", You have enough credits to pass level 2 NCEA")                                        ##
        return True                                                                                          ##
    else:                                                                                                  ##
        remaining = (LEVEL2 - total)                                                                         ## repeated code from function for Level 1, except with variables for Level 2
        print (name, ", You need {} more credits to pass level 2 NCEA".format(remaining))                    ## could be merged into a single function with placeholders for the user's level (see bottom of file)

def passLevel3(total):                                                                                       ##
    if total >= LEVEL3:                                                                                      ##
        print (name,", You have enough credits to pass level 3 NCEA")                                        ##
        return True                                                                                          ##
    else:                                                                                                    ##
        remaining = (LEVEL3 - total)                                                                         ## repeated code from function for Level 1, except with variables for Level 3
        print (name,", You need {} more credits to pass level 3 NCEA".format(remaining))                     ## could be merged into a single function with placeholders for the user's level (see bottom of file)

def endorsment(meritEnd):                                                                                    ## create a function with the name endorsment (sic) and the redundant placeholder 'meritEnd' (already a variable, can be referenced within the function w/o being an argument)
    if excellence >= 50:                                                                                     ##     if the user has over 50 Excellence credits:
        print (name,", You have gained an Excellence Endorsment ")                                           ##         tell the user they have attained an Endorsement at Excellence level
        
    elif meritEnd >= 50:                                                                                     ##     if the user has over 50 Merit credits:
        print (name,", You have gained a Merit Endorsment ")                                                 ##         tell the user they have attained an Endorsement at Merit level
        remainingExc = (50 - excellence)                                                                     ##         set a variable to the amount of Excellence credits the user still needs to attain Excellence endorsed
        print (name,", You need {} more E credits to recieve an Excellence Endorsment".format(remainingExc)) ##         tell the user how many credits they still need for Excellence endorsed
    else:                                                                                                    ##     if the user doesn't have 50 credits at either Merit or Excellence:
        remainingEnd = (50 - meritEnd)                                                                       ##         set a variable to the amount of credits at M or E they still need to attain at least a Merit endorsement
        print (name,", You need {} more M or E credits to recieve a Merit Endorsment".format(remainingEnd))  ##         tell the user how many credits at M or E they still need to attain at least a Merit endorsement

def university():                                                                                            ## create a function with the name university
    numeracy = int(input("How many Numeracy credits did you gain in level 1 and 2? "))                       ##     ask the user how many Numeracy credits they've attained, and assign it to a variable
    literacy = int(input("How many Literacy credits did you gain in level 2? "))                             ##     ask the user how many Literacy credits they've attained, and assign it to a variable
    if uniEntrance >= 3 and numeracy >= 10 and literacy >= 10:                                               ##     if the user has attained University Entrance:
        print ("Congratulations {}! You have gained University Entrance!".format(name))                      ##         tell the user that they have attained UE
    else:                                                                                                    ##     if the user hasn't yet attained University Entrace:
        print (name,", It appears you are still working towards University Entrance,")                       ##         tell the user they haven't yet attained UE


subjectCredits = {}                                                                                          ## initialise an empty dictionary with the name subjectCredits


print("Welcome to your NCEA Credit Calculator!")                                                             ## print a welcome message to the user

name = input("What is your name? ")                                                                          ## ask the user what their name is, and assign input to a variable
year = int(input("What is your year level? level 1, 2 or 3: "))                                              ## ask the user what their current Level of study is, and assign it to a variable

check = "y"                                                                                                  ## create a variable which will allow the user to tell the program when they have finished entering all their subjects

while check == "y":                                                                                          ## while the user hasn't finished entering their subjects:
    subject = input("Enter a subject that you have taken this year: ")                                       ##     ask the user to enter one of their subjects, and assign it to a temporary variable
    subjectCredits[subject] = {'a':0, 'm':0, 'e':0}                                                          ##     add the user's subject to the subjectCredits dictionary as the key, and a dictionary for the user's credits in that subject as the value
    
    while True:                                                                                              ## repeat the following forever until told to break:
        check = input("Would you like to add another subject? y/n ")                                         ##     ask the user if they would like to enter another subject, and assign it to a variable

        if check == "n":                                                                                     ##     if the user has finished entering in all their subjects:
            check = "n"                                                                                      ##         redundant line (if a = b, set a = b)
            break                                                                                            ##         break the infinite loop and move on
        elif check == "y":                                                                                   ##     if the user still has subjects to enter:
            break                                                                                            ##         break and go back to input subjects
        else:                                                                                                ##     if the user gave an invalid input (not 'y' or 'n')
            print("Please enter a valid option ")                                                            ##         tell the user to enter a valid input


for i in subjectCredits:                                                                                     ## for each key in the subjectCredits dictionary:
    print("For", i.title())                                                                                  ##     tell the user the subject currently being run in title case {subject names are the keys in the subjectCredits dictionary}
    for key,value in subjectCredits[i].items():                                                              ##     for each credit level (Achieved, Merit, Excellence) in the [subject]:
        subjectCredits[i][key] = int(input("How many {} credits did you gain? " .format(key.upper())))       ##         ask the user how many credits they attained at each level in that subject, and change the appropriate value in the subject's dictionary
        

total = 0                                                                                                    ## 
achieved = 0                                                                                                 ##
merit = 0                                                                                                    ##
excellence = 0                                                                                               ## initialise the specified variable names with empty values


for subjectKeys,subjectValues in subjectCredits.items():                                                     ## for each subject and each subject's dictionary of credits:
    
    subjectTotal = sum(subjectValues.values())                                                               ##     add the total number of credits attained at all levels in the subject and assign it to a variable
    if subjectTotal >= 14:                                                                                   ##     if the user attained more than 14 credits in the subject:
        uniEntrance = uniEntrance + 1                                                                        ##         increase the number of UE subjects the user has passed by 1 (though this could be incorrect, as not EVERY subject is UE)
        
    for markKeys,markValues in subjectValues.items():                                                        ##     for each credit level (A, M, E) and respective number of credits in each subject:
        total = (total + markValues)                                                                         ##         increase the user's total number of credits by the number of credits in the current credit level
        if markKeys == 'a':                                                                                  ##         if the Achieved key is currently being run:
            achieved = (achieved + markValues)                                                               ##             increase the user's total number of Achieved credits by the number of Achieved credits attained in the subject
        elif markKeys == 'm':                                                                                ##         if the Merit key is currently being run:
            merit = (merit + markValues)                                                                     ##             increase the user's total number of Merit credits by the number of Merit credits attained in the subject
        elif markKeys == 'e':                                                                                ##         if the Excellence key is currently being run:
            excellence = (excellence + markValues)                                                           ##             increase the user's total number of Excellence credits by the number of Excellence credits attained in the subject
        
print ("\nYour total amount of credits for the year is: ", total)                                            ## tell the user the total amount of credits they've attained

print ("\nYour total amount of Achieved credits: ", achieved)                                                ## 
print ("Your total amount of Merit credits: ", merit)                                                        ## 
print ("Your total amount of Excellence credits: ", excellence)                                              ## tell the user the total amount of credits they've attained at Achieved, Merit and Excellence respectively

meritEnd = (merit + excellence)                                                                              ## add the total number of Merit and Excellence credits the user attained and assign it to a variable
if year == 1:                                                                                                ## if the user is studying Level 1:
    passed = passLevel1(total)                                                                               ##     call the passLevel1 function and assign the returned value (True, None) to a variable
    if passed == True:                                                                                       ##     if the returned value is True (i.e. they have enough to pass):
        endorsment(meritEnd)                                                                                 ##         call the endorsment function
        
if year == 2:                                                                                                ##
    passed = passLevel2(total)                                                                               ##
    if passed == True:                                                                                       ## repeated code from above conditional statement for Level 1 except with variables and functions for Level 2
        endorsment(meritEnd)                                                                                 ## could be merged into a single function which is called with placeholders (arguments) for the user's level (see bottom of file)

if year == 3:                                                                                                ##
   passed = passLevel3(total)                                                                                ##
   if passed == True:                                                                                        ## repeated code from above conditional statement for Level 1 except with variables and functions for Level 2
        endorsment(meritEnd)                                                                                 ## could be merged into a single function which is called with placeholders (arguments) for the user's level (see bottom of file)
        university()                                                                                         ##         call the university function
print ("Thank you for using the NCEA credit calculator! Goodbye.")                                           ## print a goodbye message to the user
sys.exit()                                                                                                   ## exits the program (redundant, the program will end anyways as this is the final line)

## def passLevel(userLevel, printLevel):
##     if total >= userLevel:
##         print (name,", You have enough credits to pass level {} NCEA".format(printLevel))
##         return True
##     else:
##         remaining = (userLevel - total)
##         print (name, ", You need {} more credits to pass level {} NCEA".format(remaining, printLevel))
##
## def calculator(userLevel, printLevel):
##     passed = passLevel(userLevel, printLevel)
##     if passed == True:
##         endorsment(meritEnd)
##     if year == 3:
##         university()
##
## if year == 1:
##     calculator(LEVEL1, "1")
##
## if year == 2:
##     calculator(LEVEL2, "2")
##
## if year == 3:
##     calculator(LEVEL3, "3")
