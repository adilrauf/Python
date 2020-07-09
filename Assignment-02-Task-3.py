# Assignment 02. Task 3
                            # AUTHOR: ADIL RAUF

# Write a Python program which iterates the integers from 1 to 50. For multiples of
# three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz

# Range of Numbers to be checked for
# Iterative series
a = 1;  c = 50

# Variable initialization
i = 0

for i in range (a,c+1):
    if (i%3 == 0) or (i%5 == 0):
        if (i%3 == 0) and (i%5 == 0):
            print ('fizzbuzz')
        if (i%3 == 0) and (i%5 != 0):
            print('fizz')
        if (i%5 == 0) and (i%3 != 0):
            print('buzz')
    else:
        print(i)
