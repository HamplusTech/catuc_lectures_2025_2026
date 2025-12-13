class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount, name):
        if amount > 0:
            self.__balance += amount
            return f"A deposit of {amount} by {name} was successful. New balance is {self.__balance}. Congrats!"
        return f"You can't deposit {amount} amount"
    
    def withdraw (self, amount, name):
        if name != self.owner:
            return f"You are not the owner. This account belongs to {self.owner}"
        if amount > self.__balance:
            return f"Insufficient fund. Present account balance is {self.__balance}"
        elif amount == self.__balance:
            return f"You can't withdraw. Reason: You must have a minimum balance of 2000 and present balance is {self.__balance}"
        self.__balance -= amount
        return f"You ({name}) just withdrew {amount}. Thank you for banking with Z2H bank!"


user1 = BankAccount("Uche")
user2 = BankAccount("Irene", 2000)

# print(user1.deposit(3000, "Precious"))
# print(user2.deposit(500, "Tanya"))

# print("I want to withdraw")

# print(user1.withdraw(2000, "Precious"))
# print(user2.withdraw(2500, "Irene"))

# print("Successful conditions")

# print(user2.withdraw(500, "Irene"))
# print(user1.withdraw(1000, "Uche"))

# print(user1.__balance) # this can't be access. it shows that it is hidden (encapsulated)

