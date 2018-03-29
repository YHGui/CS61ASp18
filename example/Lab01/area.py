from math import pi, sqrt

def area(r, shape_constant):
	assert r > 0, 'A length must be positive'
	return r * r * shape_constant
def area_square(r):
	return area(r, 1)

def  area_circle(r):
	return area(r, pi)

def area_hexagon(r):
	return area(r, sqrt(3) * 3 / 2)

