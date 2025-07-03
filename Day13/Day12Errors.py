# In day 12 when we wrote the code of a banking system in the encapsulation file, 
# we breached encapsulation by directly accessing the receiver's money using
# receiver.__balance += transfer_amount.
# Even though this line was inside the class, it accessed the private data
# of another object, which violates the core idea of encapsulation.
# Encapsulation means that each object is fully responsible for managing
# its own internal state — no other object should interfere directly.
# In the corrected version below, we maintain proper encapsulation by:
# Letting the receiver object handle its own balance through its public method:
# receiver.deposit(amount)
# This way:
# We do not touch the private variable __balance of another object and 
# the transfer method now follows proper encapsulation principles.

# Fixed code:
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
        receiver.deposit(transfer_amount)
        return f'The amount of {transfer_amount} is transferred successfully. The new balance is {receiver.get_balance()}.'  

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
