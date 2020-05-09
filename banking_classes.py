# Your program will use the inheritance diagram in order to create a parent class and two child classes
# Your program will create an object of each type (CheckingAccount and SavingsAccount). 
# Your program will use the following data:
# Balance: $100, $25
# Fees: $5
# Minimum Balance $50
# Interest Rate: 2%
# You will need to run the program twice.  
# Once with the account balance of $100 and once with the account balance of $25. 
# The second run of the program will have a balance lower than the minimum balance.
# A message should be output letting the user know that their account is below the minimum balance.  
# Incorporate the good coding practices you have learned up to this point in the course such as Try/Except Blocks.
# Allow the user to continue to run the program and to exit the program, formatting methods, etc.

class BankAccount(): #create the parent class 
    def __init__(self,accountNumber,balance): #defines the attributes related to the parent class
        self.accountNumber=accountNumber
        self.balance=balance

    def withdraw(self,amount): #function to withdraw, if and else used to check inputs
        amount = float(input('How much would you like to withdraw?'))
        if amount<0:
           print('Withdrawn amount can not be a negative value.')
        if amount>self.balance:
           print('insufficient balance')
        else:
            self.balance-=amount #removes withdrawn amount from balance

    def deposit(self,amount): #function to deposit, uses if to check inputs
        amount = float(input('How much would you like to deposit?'))
        if amount<0:
            print('Can not deposit negative amount.')
        else:    
            self.balance += amount #adds deposited amount to balance

    def getBalance(self): #displays the current balance
        print(f'Account Number {self.accountNumber} has a current balance of {self.balance}')


class CheckingAccount(BankAccount): #child class to bankAccount
    def __init__(self,accountNumber,balance,fees,minimumBalance): #defines attributes of the child
        super().__init__(accountNumber,balance)
        self.fees = 5
        self.minimumBalance = 50

    def deductFees(self):
        if self.balance < self.minimumBalance:
            print(f'${self.fees} was removed for maintaining insufficient balance.')
            self.balance -= self.fees

    def checkMinimumBalance(self):
        print(f'{self.minimumBalance()} is the minimum account balance')


class SavingsAccount(BankAccount): #child class to bankAccount
    def __init__(self,accountNumber,balance,interestRate): #defines attributes of the child
        super().__init__(accountNumber,balance)
        self.interestRate = 2

    def addInterest(self):
        interest = self.getBalance()*self.interestRate/100


large_account = BankAccount('505', 100)
print(large_account.getBalance)


small_account = CheckingAccount('404', 25,(),())
small_account.checkMinimumBalance()
print(small_account.getBalance)
