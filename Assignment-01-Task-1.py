# Assignment 01, Task-01
                            # AUTHOR: ADIL RAUF

# Number of previous car accidents
# less than 5: zero increase
# between 5 and 10: increase $25
# between 11 and 20: increase $50
# 21 or more: increase $100


Number_of_Accidents = 0
cost = 0
Number_of_Accidents = int(input("Enter number of accidents : "))

if (Number_of_Accidents >= 5 and Number_of_Accidents <= 10 ):
  cost = 25
if (Number_of_Accidents >= 11 and Number_of_Accidents <= 20 ):
  cost = 50
if (Number_of_Accidents >= 21):
  cost = 100

if (cost == 0):
  print('No increase in Insurance Cost as Number of accidents are less than 5')
elif (cost != 0):
  print('Increase in Insurance Cost in $ =',cost)
  print('Number_of_Accidents =',Number_of_Accidents)
