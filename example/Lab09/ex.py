from operator import add, mul, truediv

def invert(x):
	y = 1 / x
	print('Never printed if x is 0')
	return y

def invert_safe(x):
	try:
		return invert(x)
	except ZeroDivisionError as e:
		print('handled', e)
		return 0

def divide_all(n, ds):
	try:
		return reduce(truediv, ds, n)
	except ZeroDivisionError as e:
		return float('inf')
	else:
		pass
	finally:
		pass

def reduce(f, s, initial):
	
	"""Combine elements of s using f with initial

	>>> reduce(mul, [2, 4, 8], 1)
	64
	>>> reduce(add, [1, 2, 3, 4], 0)
	10
	"""
	for x in s:
		initial = f(initial, x)
	return initial

def reduce(f, s, initial):
	
	"""Combine elements of s using f with initial

	>>> reduce(mul, [2, 4, 8], 1)
	64
	>>> reduce(add, [1, 2, 3, 4], 0)
	10
	"""
	if not s:
		return initial
	else:
		first, rest = s[0], s[1:]
		return reduce(f, rest, f(initial, first))