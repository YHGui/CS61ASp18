def gcd(m, n):
	"""Returns the largest k that divides both m and n.
	k, m, n are all positive integers.
	>>> gcd(12, 8)
	4
	>>> gcd(16, 12)
	4
	>>> gcd(16, 8)
	8
	>>> gcd(2, 16)
	2
	>>> gcd(5, 5)
	5
	"""
	if m == n:
		return m
	elif m < n:
		return gcd(n, m)
	else:
		return gcd(m - n, n)
def trace1(fn):
	"""Returns a version of fn that first print when it is 
	called

	fn - a function of 1 argument
	"""
	def traced(x):
		print('Calling', fn, 'on argument', x)
		return fn(x)
	return traced

def curry2(f):
	def g(x):
		def h(y):
			return f(x, y)
		return h
	return g

@trace1
def square(x):
	return x * x
@trace1
def sum_square_up_to(n):
	k, total = 1, 0
	while k <= n:
		total, k = total + square(k), k + 1
	return total