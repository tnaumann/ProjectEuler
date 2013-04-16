"""
Project Euler (http://projecteuler.net/)
Problem 9
"""

def solution():
	products = (a * b * (1000 - (a + b))
		for a in range(1, 500)
		for b in range(a, 500)
		if a**2 + b**2 == (1000 - (a + b))**2
	)

	return next(products)	# there is exactly one

if __name__ == "__main__":
	print(solution())