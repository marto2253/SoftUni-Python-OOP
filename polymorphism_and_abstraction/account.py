class Account:
    def __init__(self, owner, amount = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount - sum(self._transactions)

    def validate_transaction(self, account: Account, amount_to_add):
        if self.balance - amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!" )
        return f"New balance: {account.balance}"