#-----------------------------------------------------------------------------
#PYTHON CODE TO CONVERT A BASE 10 NUMBER TO ANOTHER BASE (Base 2 thru Base 16)
#-----------------------------------------------------------------------------

# 1. Develop the ALGORITHM for converting decimal number to a new base
#-------------------------------------------------------------------------
#   Input the new base, decimal number
#   While (the quotient is not zero)
#      	    Divide the decimal number by the new base
#	    Make the remainder the next digit to the left in the answer
#	    Replace the original decimal number with the quotient
#   Output the answer
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# 2. Convert the ALGORITHM to PSEUDOCODE 
#-------------------------------------------------------------------------
#Write "Enter the new base"
#Read newBase
#Write "Enter the number to be converted"
#Read decimalNumber
#Set quotient to 1
#Set answer to ""
#WHILE (quotient is not zero)
#		Set quotient to decimalNumber DIV newBase
#		Set remainder to decimalNumber REM newBase
#		Make the remainder the next digit to the left in the answer
#		Set decimalNumber to quotient
#Write "The answer is "
#Write answer
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# 3. Convert the PSEUDOCODE into PYTHON CODE
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
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# 4. More Python code to Verify the answer is correct
#------------------------------------------------------------------------
    answerLength = len(answer)
    proofAnswer = 0
    exponent = answerLength-1
    for digit in answer:
        if digit =="A":
            dig = "10"
        elif digit == "B":
            dig = "11"
        elif digit == "C":
            dig = "12"
        elif digit == "D":
            dig = "13"
        elif digit == "E":
            dig = "14"
        elif digit == "F":
            dig = "15"
        else:
            dig = digit    
        proofAnswer = proofAnswer + (int(dig)*newBase**exponent)
        print(digit+" x "+str(newBase)+"^"+str(exponent)+" = "+str(proofAnswer)+" +")    
        exponent = exponent -1
    if proofAnswer == originalDecimalnumber:
        print ("The base-"+ str(newBase) +" answer "+answer+ " is equal to the original base-10 number "+str(originalDecimalnumber))
    else:
        print (str(proofAnswer)+" is not equal to the orignal decimalNumber "+str(originalDecimalnumber))
    
