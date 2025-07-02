# Creating a banking system.

# Create a class called BankAccount with:
# A private variable to store balance
# A method to get the balance
# A method to update the balance only if the amount is positive

# Task 2:
# Enhance your BankAccount class to include:
# A method to deposit money (must be positive)
# A method to withdraw money (must not exceed balance)
# Print the updated balance after each successful operation
# Rules:
# Don't touch __balance directly from outside
# Stick to using methods

# Task 3:
# Add a method to your BankAccount class that allows one account to transfer money to another account.
# Requirements:
# The method should:
# Take another BankAccount instance as the receiver
# Subtract money from the sender (if enough balance)
# Add money to the receiver
# Print or return a confirmation message
# Bonus Constraints:
# Don't break encapsulation meaning don't access receiver.__balance directly 
# Make sure transfers don't happen if insufficient funds
# Add clear, user-friendly messages like we did in withdraw

class BankAccount:
    def __init__ (self, balance):
        self.__balance = balance
    def get_balance(self):              # Getter
        return self.__balance   
    def update_balance(self, amount):   # Setter
        if amount > 0:
            self.__balance = amount
        else:
            print('The entered amount is invalid.')
    def deposit(self,deposited_amount):
        self.__balance += deposited_amount
        return f'The balance after this deposit of {deposited_amount} is: {self.get_balance()}'
    def withdraw(self, money_to_be_withdrawn):
        if money_to_be_withdrawn > self.__balance:
            return f'The entered amount of {money_to_be_withdrawn} is more than your current balance of {self.get_balance()} .'
        else:
            self.__balance -= money_to_be_withdrawn
            return f'The balance after this withdrawal of {money_to_be_withdrawn} is: {self.get_balance()}'
    def transfer(self, receiver, transfer_amount):
        if transfer_amount <= 0:
            return f'The amount of {transfer_amount} is invalid.'
        if transfer_amount > self.__balance:
            return f'The amount of {transfer_amount} could not be transferred due to insufficient balance of {self.__balance}.'
        self.__balance -= transfer_amount
        receiver.__balance += transfer_amount
        return f'The amount of {transfer_amount} is transferred successfully. The new balance is {receiver.__balance}.'  

obj = BankAccount(50000)
print(obj.get_balance())
obj.update_balance(60000)
print(obj.get_balance())
obj.update_balance(-1)
print(obj.get_balance())

# Task - 2: 
print(obj.deposit(20000))
print(obj.withdraw(40000))
print(obj.withdraw(100000000))

# Task -3:
obj2 = BankAccount(100)
print(obj.transfer(obj2, 1500))
