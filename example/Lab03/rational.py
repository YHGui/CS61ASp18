# Rational arithmetic

def add_rational(x, y):
	nx, dx = numer(x), denom(x)
	ny, dy = numer(y), denom(y)
	return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
	return rational(numer(x) * numer(y), denom(x) * denom(y))

def rational_are_equal(x, y):
	return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
	print(numer(x), "/", denom(x))


# Constructor and selectors

def rational(n, d):
	"""Construct a rational number x that represents n/d"""
	def select(name):
		if name == 'n':
			return n
		elif name == 'd':
			return d
	return select
	#return [n, d]

def numer(x):
	"""Return the numerator of rational number x."""
	return x('n')
	#return x[0]

def denom(x):
	"""Return the denominator of ration number x."""
	return x('d')
	#return x[1]