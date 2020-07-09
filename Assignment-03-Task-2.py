# Assignment 03, Task-02
                            # AUTHOR: ADIL RAUF
# Task 2
# Write a Python program to get the largest number from a list.
# Sample List :
# [1, 4, 5, 9]
# Expected output:
# 9

# Initialization
i = 0; j = 0; Comparison_Value = 0
list = []

# Input
Number_of_Elements = int(input("Enter number of elements in the LIST : "))

# Formation of List
for i in range(0, Number_of_Elements):
    List_Element = int(input("Enter LIST element no:" + str(i+1) + " = "))
    list.append(List_Element)

# Largest number in the List
Comparison_Value = list[0]
for j in range(0, len(list)):
        if Comparison_Value < list[j]:
            Comparison_Value = list[j]

# Output
print("                                   ")
print("OUTPUT")
print("___________________________________")
print("       List =", list)
print("Larget Number =", Comparison_Value)
print("___________________________________")