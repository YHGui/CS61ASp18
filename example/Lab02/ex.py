#from ucb import trace

def search(f):
	x = 0
	while True:
		if f(x):
			return x
		x += 1

def is_three(x):
	return x == 3

def square(x):
	return x * x

def positive(x):
	return max(0, square(x) - 100)

def inverse(f):
	"""Return g(y) such that g(f(x)) -> x."""
	return lambda y: search(lambda x: f(x) == y)

def split(n):
	return n // 10, n % 10

def sum_digits(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return sum_digits(all_but_last) + last

def luhn_sum(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
	all_but_last, last = split(n)
	luhn_digit = sum_digits(last * 2)
	if n < 10:
		return luhn_digit
	else:
		return luhn_sum(all_but_last) + luhn_digit

def sum_digits_iter(n):
	digit_sum = 0
	while n > 0:
		n, last = split(n)
		digit_sum = digit_sum + last
	return digit_sum

def sum_digits_rec(n, digit_sum):
	if n == 0:
		return digit_sum
	else:
		n, last = split(n)
		return sum_digits_rec(n, digit_sum + last)

def cascade(n):
	if n < 10:
		print(n)
	else:
		print(n)
		cascade(n // 10)
		print(n)
def cascade2(n):
	print(n)
	if n >= 10:
		cascade2(n // 10)
		print(n)
grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)
def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

#@trace
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n - 2) + fib(n - 1)

def count_partitions(n, m):
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif m == 0:
		return 0
	else:
		with_m = count_partitions(n - m, m)
		without_m = count_partitions(n, m - 1)
		return with_m + without_m