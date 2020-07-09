# Assignment 03, Task-01
                            # AUTHOR: ADIL RAUF
# Task 1
# Write a Python program to sum all the items in a list of integer numbers.
# Sample List :
# [1, 4, 5, 9]
# Expected output:
# 19

# Initialization
i = 0; j = 0
Sum_of_List_Elements = 0
list = []

# Input
Number_of_Elements = int(input("Enter number of elements in the LIST : "))

# Formation of List
for i in range(0,Number_of_Elements):
    List_Element = int(input("Enter LIST element no:" + str(i+1) + " = "))
    list.append(List_Element)

# Sum of List
for j in range(0,len(list)):
    Sum_of_List_Elements = list[j] + Sum_of_List_Elements

# Output
print("                                   ")
print("OUTPUT")
print("___________________________________")
print("       List =", list)
print("Sum of List =", Sum_of_List_Elements)
print("___________________________________")