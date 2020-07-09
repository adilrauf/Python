#                   Assignment-04 and Task 01
#                         Author: ADIL RAUF
#
# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.
# Sample Input :
# 5
# Expected output:
# 120

#   DEFINING A FUNCTION

def Factorial_function(Integer_Number):
    # INITIALIZING VARIABLE
    Multiplier = 1
    for Integer_Number in range (Integer_Number,1,-1):
        Multiplier = Multiplier*Integer_Number
    return Multiplier

#    INPUT

Integer_Number = int(input('Enter a positive integer : '))

#   CALLING THE FUNCTION AND PRINT

if Integer_Number > 1:
    print("=============================")
    print("Factorial of ",Integer_Number," is ", Factorial_function(Integer_Number))
else:
    print("Enter positive integer greater than one")
