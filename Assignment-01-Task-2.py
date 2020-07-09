# Assignment 01, Task-02
                            # AUTHOR: ADIL RAUF
# Years driving rule
# less than 5 years driving: no discount available
# between 5 and 10: give 5% discount
# between 11 and 20: give 10% discount
# more than 21: give 15% discount

Number_of_Years_of_Driving = 0
Discount = 0
Number_of_Years_of_Driving = int(input("Enter number of years of driving : "))

if (Number_of_Years_of_Driving >= 5 and Number_of_Years_of_Driving <= 10 ):
  Discount = 5
if (Number_of_Years_of_Driving >= 11 and Number_of_Years_of_Driving <= 20 ):
  Discount = 10
if (Number_of_Years_of_Driving >= 21):
  Discount = 15

if (Discount == 0):
  print('No Discount available in Insurance Cost as Number of years of driving are less than 5')
elif (Discount != 0):
  print('Discount in Insurance Cost in $ =', Discount)
  print('Number_of_Years_of_Driving =', Number_of_Years_of_Driving)
