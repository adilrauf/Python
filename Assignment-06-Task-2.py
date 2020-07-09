#                   Assignment-06 and Task 02
#                     Author: ADIL RAUF
#
#   Write a python class to represent a checking account (CheckingAccount):
#       ● The class constructor should receive the owner name and initial balance.
#       ● The class should have a list attribute to store all debts and credits.
#       ● The class should have the following methods:
#            ○ debit(amount): will deduct a given amount from the balance.
#            ○ credit(amount): will add a given amount to the balance.
#            ○ print_statement(): will print all the debits and credits and the final
#              balance.
#       ● The attributes should be private while the methods should be public.

# DEFINING CLASS
class CheckingAccount:
  Transaction_List = []                                         #  Initialization of ARRAY

  def __init__(self, Owner_Name, Intitial_Balance):             #  This Constructor is PRIVATE
    self.Owner_Name = Owner_Name
    self.Intitial_Balance = Intitial_Balance

  def credit(self, credit_money):                               #  This Method is PUBLIC
    self.credit_money=credit_money
    self.Transaction_List.append(credit_money)

  def debit(self, debit_money):                                 #  This Method is PUBLIC
    self.debit_money = debit_money
    self.Transaction_List.append(debit_money)

  def print_statement(self, Dummy_Variable):                    # This method is PUBLIC
    print("("+str(self.debit_money)+")")
    print("+"+str(self.credit_money))
    Current_Balance = sum(self.Transaction_List) + self.Intitial_Balance
    if Current_Balance > 0:                                                 # Conditions for formatted output
        print("Current Balance : +"+str(Current_Balance))
    elif Current_Balance < 0:
        print("Current Balance : ("+str(Current_Balance)+")")
    elif Current_Balance == 0:
        print("Current Balance : ", Current_Balance)
    print("Transaction List :", self.Transaction_List)

#INITIALIZATION
checking = CheckingAccount("Adil", 100.0)
Dummy_Variable = 0

# INPUT
Amount_Deposit = float(input("Enter how much AMOUNT you want to DEPOSIT: "))
Amount_Draw = float(input("Enter how much AMOUNT you want to DRAW: "))
Amount_Draw = -Amount_Draw

# OUTPUT
print("==============================================")
print(checking.Owner_Name,"cheqing account statement")
checking.credit(Amount_Deposit)
checking.debit(Amount_Draw)
checking.print_statement(Dummy_Variable)


