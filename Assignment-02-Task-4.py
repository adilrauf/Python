# Assignment 02. Task 4
                            # AUTHOR: ADIL RAUF
# Write a Python program which reads from the input two numbers and then
# computes the Greatest common divisor of them and prints the result.
# Sample Input:
# 12
# 21
# Sample Output:
# 3

# Initialization of Variables
a = 2; z = 0; gcd = 1;

# Inputs
n1=int(input("Enter 1st number = "))
n2=int(input("Enter 2nd number = "))

if n1 > n2:
    z = n1
else:
    z = n2

for i in range (a,z+1):
    while (n1%i == 0 and n2%i == 0):
        gcd= i*gcd
        n1=n1/i
        n2=n2/i

print('Greatest Common Divisor =', gcd)
