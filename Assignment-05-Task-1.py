#                   Assignment-05 and Task 01
#               Author: ADIL RAUF
#
# Write a Python recursive function to calculate the factorial of a number (a
# non-negative integer). The function accepts the number as an argument.
# Sample Input :
# 5
# Expected output:
# 120

# RECURSION FUNCTION
def Factorial(Integer):

    if (Integer == 1) or (Integer < 1):
        return 1
    return Integer * Factorial(Integer-1)

# INPUT
Integer = int(input("Enter an integer to find out its factorial: "))

# PRINT
print('Factorial of', Integer,' = ',Factorial(Integer))