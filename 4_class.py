# 4. class variable and class method 

class Bank:
    bank_name = "HBL Bank"
    
    def __init__(self, acc_user):
        self.acc_user = acc_user
        
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        
    def display(self):
        print(f"Account holder: {self.acc_user}, Bank : {self.bank_name}")
        
account1 = Bank("Faria")
account2 = Bank("usman")

account1.display()
account2.display()

Bank.change_bank_name("UBL Bank")

account1.display()
account2.display()