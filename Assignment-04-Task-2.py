#                   Assignment-04 and Task 02
#                       Author: ADIL RAUF
#
# Write a Python function that checks whether a passed string is palindrome or not.
# Sample Input 1:
# civic
# Expected output 1:
# True
# Sample Input 2:
# canada
# Expected output 2:
# False

#   DEFINING A FUNCTION

def Palindrome_function(Input_String):
    # INITIALIZING VARIABLE
    Loop_Starter = 0;  Decide = 'YES';

    # LOOP FOR COMPARING ARRAY ELEMENTS IN REVERSE ORDERS AND RUNS UNTIL THE ELEMENTS ARE SAME OTHERWISE BREAKS THE LOOP
    for Loop_Starter in range (len(Input_String),0,-1):
        if Input_String[len(Input_String) - Loop_Starter] != Input_String[Loop_Starter - 1]:
            Decide = 'NO'
            break

    # PRINTS BASED ON THE DECIDE VARIABLE
    if Decide == 'YES':
       print('=======================')
       print('True')
    elif Decide == 'NO':
       print('=======================')
       print('False')

    return


# INPUT
Input_String = input("Enter a String : ")

# CALLS THE FUNCTION
Palindrome_function(Input_String)


