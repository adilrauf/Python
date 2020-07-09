#                   Assignment-05 and Task 02
#                     Author: ADIL RAUF
#
# Write a Python recursive function to calculate the sum of a list of numbers.
# Sample List :
# [1, 3, 5, 6]
# Expected output:
# 15

# RECURSION FUNCTION
def Sum_of_List(Array,Array_Index,Sum):
    # CONDITION TO CHECK IF ALL THE ARRAY ELEMENTS MANIPULATED
    if Array_Index > len(Array)-1:
         return Sum
    return Array[Array_Index]+Sum_of_List(Array,Array_Index+1,Sum)

# INPUT
Number_of_Elements = int(input("Enter how many elements in a LIST: "))

# INITIALIZATION
Array=[]; Array_Index = 0; Sum = 0

for i in range(0,Number_of_Elements):
    List_Element = int(input("Enter "+ str(i+1)+" of the LIST: "))
    Array.append(List_Element)

print ('Sum of Array is = ', Sum_of_List(Array,Array_Index,Sum))
