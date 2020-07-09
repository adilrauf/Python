# Assignment 02. Task 1
                            # AUTHOR: ADIL RAUF
# Write a Python program to find those numbers which are divisible by 7 and
# multiple of 5, between 1500 and 2700 (both included)

# Range of Numbers to be checked for
# Divisbility and Multiplicity
a = 1500; b = 2700;

# Variable initialization
i=0; j=0; k=0; l=0


print('Numbers Divisible by 7')
print('======================')
for i in range (a,b+1):
    if i%7 == 0:
        print (i)
print('======================')
print(' ')


print('Numbers Multiple of 5')
print('======================')
for i in range (a,b+1):
    if i%5 == 0:
        print (i)
print('======================')
