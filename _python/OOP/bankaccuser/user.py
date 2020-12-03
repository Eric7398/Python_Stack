from bank import BankAccount

class User:		
    # Attributes
    def __init__(self, name, email, bank):
        self.name = name
        self.email = email
        self.account = BankAccount (int_rate=0.02, balance=0)
        
    
    # Methods
    def display_user_balance(self):
        print (f"{self.name}, Balance: {self.account.balance} \n")
        return self	
        
    def make_deposit(self, amount, bank):	
        self.account.deposit
        return self
    
    def make_withdrawal(self, amount, bank):
        self.account.withdraw	
        return self
    
    def transfer(self, amount, other):
        self.account.withdraw
        other.account.deposit
        if self.account.balance < 0:
            print(f"{self.name} you gotta go back on the hussle because you're in debt!")
        return self


john = User("John", "John@example.com", "Checking")

# eric = User("Eric", "Eric@example.com", "accountB")

john.make_deposit(500, "Checking").display_user_balance()

#ok idk anymore my mental is about to go boom, I give up on the sensei challenge for now



