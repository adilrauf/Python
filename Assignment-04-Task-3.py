#                   Assignment-04 and Task 03
#               Author: ADIL RAUF
#
# Write a Python function to check whether a passed number is perfect or not.
# Sample Input 1 :
# 6
# Expected output 1:
# True
# Sample Input 2 :
# 3
# Expected output 2:
# False

# LIST OF PERFECT NUMBERS: 6, 28, 496, 8128, 33550336, 8589869056


#   DEFINING A FUNCTION

def Perfect_Number_function(Input_Number):
    # INITIALIZING VARIABLE
    Array_of_Dividers = []

    # DIVIDING WITH NUMBERS AND THE DIVIDER IS SAVED IN ARRAY IF THERE IS NO REMAINDER
    for Divider in range (1,Input_Number-1,1):
        #print(Divider)
        if Input_Number%Divider == 0:
            Array_of_Dividers.append(Divider)

    # PRINTS TRUE OF FALSE IS THE NUMBER IS PERFECT OR NOT
    if sum(Array_of_Dividers) == Input_Number:
        print('True')
    else:
        print('False')

    return

# INPUT
Input_Number = int(input("Enter a positive integer : "))

# CALLS THE FUNCTION
Perfect_Number_function(Input_Number)


