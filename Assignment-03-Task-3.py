# Assignment 03, Task-03
# AUTHOR: ADIL RAUF
# Task 3
# Write a Python program to remove duplicates from a list.
# Sample List :
# [1, 4, 4, 9, 2, 3, 1]
# Expected output:
# [1, 4, 9, 2, 3]

# Initialization
list =[]; Duplicate_Removed_List =[]

# Input
Number_of_Elements = int(input("Enter number of elements in the LIST : "))

# Formation of List
for i in range(0, Number_of_Elements):
    List_Element = int(input("Enter LIST element no:" + str(i) + " = "))
    list.append(List_Element)

for i in list:
    if i not in Duplicate_Removed_List:
        Duplicate_Removed_List.append(i)

print("The list after removing duplicates : ", Duplicate_Removed_List)


