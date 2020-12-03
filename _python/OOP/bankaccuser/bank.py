class BankAccount:
    
    def __init__(self, int_rate=0.02, balance=0):
        self.interest = int_rate
        self.balance = balance
        

    def deposit(self, amount):
        self.balance += amount
        return self 
    
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficent funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Account currently has, {self.balance}\n")
        return self
    
    def yield_interest(self):
        money = 0
        if self.balance > 0:
            money = self.balance * self.interest
            self.balance += money
            return self
        else:
            print("You have no money for interest bruh")
            return self



Checking = BankAccount(balance=500)



Saving = BankAccount(balance=1000)
