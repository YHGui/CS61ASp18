def cube(k):
	return pow(k, 3)

def summation(n, term):
	"""Sum the first n terms of a sequence

	>>> summation(5, cube)
	225
	"""
	total, k = 0, 1
	while k <= n: 
		total, k = total + term(k), k + 1

	return total