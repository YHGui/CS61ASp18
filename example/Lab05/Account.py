class Account:
	"""docstring for Account"""
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
		