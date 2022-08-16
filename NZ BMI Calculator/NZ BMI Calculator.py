import sys

validEthnicities = ["NZ European", "Pacific Island", "Maori", "Asian", "Indian"]
validityCheck = ["Yes", "No"]

euroUnderweight = 18.5
euroHealthy = 18.5
euroOverweight = 25
euroObese = 30

maoUnderweight = 18.5
maoHealthy = 18.5
maoOverweight = 26
maoObese = 32

asiaUnderweight = 18.5
asiaHealthy = 18.5
asiaOverweight = 23
asiaObese = 25

userValidity = "0"
userEthnicity = "0"
userWeight = 0.0
userHeight = 0.0

disclaimer = "\n\nPlease note that your Body Mass Index (BMI) is only a general indication of health, and you should consult your doctor with any concerns."

print("Welcome to the New Zealand BMI Calculator v1!\n")

while userValidity not in validityCheck:
    userValidity = input("Are you under 18, shorter than 1.5m, taller than 1.9m, an athlete or bodybuilder, currently pregnant or breastfeeding?\n")

    if userValidity == "Yes":
        print("Unfortunately you are currently ineligible for this BMI calculator, sorry!")
        sys.exit()

    elif userValidity not in validityCheck:
        print("You must enter either 'Yes' or 'No'.\n")

while userEthnicity not in validEthnicities:
    userEthnicity = input("\nPlease enter your ethnicity.\n")

    if userEthnicity not in validEthnicities:
        print ("You must enter either '" + validEthnicities[0] + "', '" + validEthnicities[1] + "', '" + validEthnicities[2] + "', '" + validEthnicities[3] + "' or '" + validEthnicities[4] + "'.")

while userWeight < 40.0 or userWeight > 160.0:
    userWeight = float(input("\nPlease enter your weight in kilograms.\n"))

    if userWeight < 40.0:
        print("The minimum weight is 40.0 kilograms.")

    elif userWeight > 160.0:
        print("The maximum weight is 160.0 kilograms.")

while userHeight < 1.5 or userHeight > 1.9:
    userHeight = float(input("\nPlease enter your height in metres.\n"))

    if userHeight < 1.5:
        print("The minimum height is 1.5 metres.")

    elif userHeight > 1.9:
        print("The maximum height is 1.9 metres.")

userBMI = float(round(userWeight/userHeight**2,1))

def nzEuro():
    if userBMI < euroUnderweight:
        print("You are classed as underweight with a BMI score of " + str(userBMI) + ".\n\nThis places you at a low risk of obesity related diseases." + disclaimer)

    elif userBMI >= euroHealthy and userBMI < euroOverweight:
        print("You are classed as a healthy weight with a BMI score of " + str(userBMI) + ".\n\nThis places you at a normal risk of obesity related diseases." + disclaimer)

    elif userBMI >= euroOverweight and userBMI < euroObese:
        print("You are classed as overweight with a BMI score of " + str(userBMI) + ".\n\nThis places you at a high risk of obesity related diseases." + disclaimer)

    elif userBMI >= euroObese:
        print("You are classed as obese with a BMI score of " + str(userBMI) + ".\n\nThis places you at a very high risk of obesity related diseases." + disclaimer)

def pacMaori():
    if userBMI < maoUnderweight:
        print("You are classed as underweight with a BMI score of " + str(userBMI) + ".\n\nThis places you at a low risk of obesity related diseases." + disclaimer)

    elif userBMI >= maoHealthy and userBMI < maoOverweight:
        print("You are classed as a healthy weight with a BMI score of " + str(userBMI) + ".\n\nThis places you at a normal risk of obesity related diseases." + disclaimer)

    elif userBMI >= maoOverweight and userBMI < maoObese:
        print("You are classed as overweight with a BMI score of " + str(userBMI) + ".\n\nThis places you at a high risk of obesity related diseases." + disclaimer)

    elif userBMI >= maoObese:
        print("You are classed as obese with a BMI score of " + str(userBMI) + ".\n\nThis places you at a very high risk of obesity related diseases." + disclaimer)

def asiaIndian():
    if userBMI < asiaUnderweight:
        print("You are classed as underweight with a BMI score of " + str(userBMI) + ".\n\nThis places you at a low risk of obesity related diseases." + disclaimer)

    elif userBMI >= asiaHealthy and userBMI < asiaOverweight:
        print("You are classed as a healthy weight with a BMI score of " + str(userBMI) + ".\n\nThis places you at a normal risk of obesity related diseases." + disclaimer)

    elif userBMI >= asiaOverweight and userBMI < asiaObese:
        print("You are classed as overweight with a BMI score of " + str(userBMI) + ".\n\nThis places you at a high risk of obesity related diseases." + disclaimer)

    elif userBMI >= asiaObese:
        print("You are classed as obese with a BMI score of " + str(userBMI) + ".\n\nThis places you at a very high risk of obesity related diseases." + disclaimer)

if userEthnicity == validEthnicities[0]:
    nzEuro()
    
elif userEthnicity == validEthnicities[1] or userEthnicity == validEthnicities[2]:
    pacMaori()
    
elif userEthnicity == validEthnicities[3] or userEthnicity == validEthnicities[4]:
    asiaIndian()
