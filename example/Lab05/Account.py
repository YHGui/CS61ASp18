class Account:
	"""docstring for Account
	An account has a balance and a holder.
	All accounts share a common interest rate.
	"""
	interest = 0.02 # A class attribute

	def __init__(self, accoun_holder):
		self.balance = 0
		self.holder = accoun_holder

	def deposit(self, amount):
		self.balance = self.balance + amount
		return self.balance	

	def withdraw(self, amount):
		if amount > self.balance:
			return 'Insufficient funds'
		self.balance = self.balance - amount
		return self.balance

class CheckingAccount(Account):
	"""base class is Account"""
	interest = 0.01
	withdraw_fee = 1
	def withdraw(self, amount):
		return Account.withdraw(self, amount + withdraw_fee)

class Bank:
	"""docstring for Bank"""
	def __init__(self):
		self.accounts = []
	
	def open_account(self, holder, amount, kind = Account):
		account = kind(holder)
		account.deposit(amount)
		self.accounts.append(account)
		return account

	def pay_interest(self):
		for a in self.accounts:
			a.deposit(a.balance * a.interest)

	def too_big_to_fail(self):
		return len(self.accounts) > 1
		