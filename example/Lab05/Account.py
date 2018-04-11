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
		
		