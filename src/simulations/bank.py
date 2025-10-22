
class Bank:
    def __init__(self):
        self.accounts = {}  # key: account_id, value: balance

    def create_account(self, account_id):
        if account_id not in self.accounts:
            self.accounts[account_id] = 0
            return True
        return False

    def get_balance(self, account_id):
        return self.accounts.get(account_id, None)

    def deposit(self, account_id, amount):
        if account_id in self.accounts and amount > 0:
            self.accounts[account_id] += amount
            return True
        return False

    def withdraw(self, account_id, amount):
        if account_id in self.accounts and 0 < amount <= self.accounts[account_id]:
            self.accounts[account_id] -= amount
            return True
        return False
    
    def transfer(self, sender, receiver, amount):
        if sender in self.accounts and receiver in self.accounts and 0 < amount <= self.accounts[sender]:
            self.accounts[sender] -= amount
            self.accounts[receiver] += amount
            return True
        return False
    
if __name__ == "__main__":
    bank = Bank()
    bank.create_account("A123")
    bank.create_account("B456")
    bank.deposit("A123", 500)
    bank.transfer("A123", "B456", 200)
    print("Balance A123:", bank.get_balance("A123"))  # Output: 300
    print("Balance B456:", bank.get_balance("B456"))  # Output: 200
