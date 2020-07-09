#                   Assignment-07 and Task 01
#                     Author: ADIL RAUF
#
#   For this task you will have to implement two classes related to bank: Person and
#   BankAccount.
#       ● For the Person class:
#           ○ Include the attributes that you consider essential.
#           ○ Include the methods that you consider essential (if any).
#       ● For the BankAccount:
#           ○ Include the attributes that you consider essential.
#           ○ Include the methods that you consider essential.
#           ○ Implement the composition relation between BankAccount and
#             Person classes.

# COMPOSITION RELATION between BANKACCOUNT and PERSON classes

from File_for_Assignment_07_Task_1 import Person

# CHILD/DERIVED Class INHERITED from BASE/PARENT Class "Person"

class Bank_Account(Person):

  def __init__(self, Owner_Name, Initial_Balance, Transaction_List):             #  Constructor
    super().__init__(Owner_Name, Initial_Balance, Transaction_List)              #  Attributes of Base Class

  def credit(self, credit_money):                                                #  This Method is PUBLIC
    self.credit_money = credit_money
    self.Transaction_List.append(credit_money)

  def debt(self, debt_money):                                                    #  This Method is PUBLIC
    self.debt_money = debt_money
    self.Transaction_List.append(debt_money)

  def print_statement(self):                                                    # This method is PUBLIC
    print("("+str(self.debt_money)+")")
    print("+"+str(self.credit_money))
    Current_Balance = sum(self.Transaction_List) + self.Initial_Balance
    if Current_Balance > 0:                                                      # Conditions for formatted output
        print("Current Balance : +"+str(Current_Balance))
    elif Current_Balance < 0:
        print("Current Balance : ("+str(Current_Balance)+")")
    elif Current_Balance == 0:
        print("Current Balance : ", Current_Balance)
    print("Transaction List :", self.Transaction_List)

# CREATING INSTANCE FROM THE INHERITED CHILD/DERIVED CLASS "Bank_Account"
Bank_Account_Details = Bank_Account("Adil", 100.0, [])

# INPUT
Amount_Deposit = float(input("Enter how much AMOUNT you want to DEPOSIT: "))
Amount_Draw = float(input("Enter how much AMOUNT you want to DRAW: "))
Amount_Draw = -Amount_Draw

# OUTPUT
print("==============================================")
print(Bank_Account_Details.Owner_Name,"cheqing account statement")
print(Bank_Account_Details.Transaction_List,"transaction list")
Bank_Account_Details.credit(Amount_Deposit)
Bank_Account_Details.debt(Amount_Draw)
Bank_Account_Details.print_statement()


