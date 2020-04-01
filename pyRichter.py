#PYTHON RICHTER SCALE CALCULATION
#Your first and last name: Neil Swagger
#Your ID:

#REQUIREMENTS:
# ask the user to "Enter the Richter scale value or -99 to end: "
# the program must end when the user enters -99
# the richter scale value entered must be greater than 0
# if the richter scale value is less than 0, the program must print  "Value must be greater than 0"
#   and the user must re-enter the richter scale value
# program must print the correct warning message for the richter scale value entered as per the accompanying diagram
# program must print only 1 warning message for each richter scale value entered
# the program must be tested so that it repeats until user enters -99
# the program must be tested so that if user enters a richter scale value less than 0,
#   "Value must be greater than 0" prints and the user must re-enter it
# the program must be tested with each of the following values to make sure the correct warning message is printed
#    8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6
#-------------------------------------------------------------------------

# HINT: Use the base number conversion program for guidance
#--------------------------------------------------------------------------------------------
# 1. Develop the ALGORITHM for Richter Scale program from the requirements and enter it below
#--------------------------------------------------------------------------------------------
"Enter the Richter scale value or -99 to end:"
from "0 to -99"
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# 2. Convert the ALGORITHM to PSEUDOCODE and enter it below
#-------------------------------------------------------------------------
doMore = True
while doMore == True:
    print()
    print("This program converts a base-10 number to another base")
    newBase = int(input("Enter the new base (2 thru 16 are acceptable, 1 to end): "))
    if newBase == 1:
        doMore = False
        continue
    decimalNumber = int(input("Enter the number to be converted: "))
    originalDecimalnumber = decimalNumber
    quotient = 1
    answer = ""
    while (quotient != 0):
        quotient = int(decimalNumber / newBase)
        remainder = str (decimalNumber % newBase)
        if remainder =="10":
            remainder = "A"
        elif remainder == "11":
            remainder = "B"
        elif remainder == "12":
            remainder = "C"
        elif remainder == "13":
            remainder = "D"
        elif remainder == "14":
            remainder = "E"
        elif remainder == "15":
            remainder = "F"
        answer = remainder + answer
        decimalNumber = quotient
    print ("The answer is: "+ answer)
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# 3. Convert the PSEUDOCODE into PYTHON CODE and enter it below
#-------------------------------------------------------------------------
"Enter the Richter scale value or -99 to end:-99"
if the richter scale value is less than 0, the program must print"Value must be greater than 0"
if richter scale value is more than or equal to 8.0 than the program must print"most sturctures fall" 
if richter scale value is more than or equal to 7.0 than the program must print"Many Buildings Destroyed"
if richter scale value is more than or equal to 6.0 than the program must print"Many buildings consideribly damaged,some collapse"
if richter scale value is more than or equal to 4.5 than the program must print"damage to poorly constructed buildings"
