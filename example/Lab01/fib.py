def fib(n):
	"""Compute the nth Fibonacci number, for N >= 1.
	"""
	pred, curr = 0, 1
	k = 1
	while k < n:
		pred, curr = curr, pred + curr
		k = k + 1
	return curr