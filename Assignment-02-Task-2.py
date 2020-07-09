# Assignment 02. Task 2
                            # AUTHOR: ADIL RAUF

# Write a Python program to get the Fibonacci series between 0 to 50.
# Note : The Fibonacci Sequence is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Sample Output :
# 1 1 2 3 5 8 13 21 34

# Range of Numbers to be checked for
# Fibonacci series
a = 0;  c = 50

# Variable initialization
b = 1; d = 0

print('Fibonacci series')
print('================')
print(b)

while d < c:
    d= a+b
    a = b
    b = d
    if d <= c:
        print(d)




