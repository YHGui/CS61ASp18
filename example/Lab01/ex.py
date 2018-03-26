"""Our first Python source file"""

from operator import floordiv, mod

def divide_exact(n, d):
	""" Return the quotient and remainder of dividing N by D.

	>>> q, r= divide_exact(2013, 10)
	>>> q
	201
	>>> r
	3
	"""
	return floordiv(n, d), mod(n, d)

def absolute_value(x):
	"""Return the absolute value of x.
	"""

	if x < 0:
		return -x
	elif x == 0:
		return 0
	else:
		return x

def choose(total, selection):
	"""Return the number of way to choose SELECTION items from TOTAL.
	choose(n, k) is typically defined in math as: n! / (n-k)! / k!

	>>> choose(5, 2)
	10
	>>> choose(20, 6)
	38760
	"""
	ways = 1
	selected = 0
	while selected < selection:
		selected = selected + 1
		ways, total = ways * total // selected, total - 1

	return ways

def what_prints():
	print('Hello World!')
	return 'Exiting this function'
	print('61A is awesome!')



