"""
Project Euler (http://projecteuler.net/)
Problem 4
"""

def solution():
	is_pal = lambda s: str(s) == str(s)[::-1]
	products = (x*y for x in range(100,1000) for y in range(x, 1000))
	return max(filter(is_pal, products))

if __name__ == "__main__":
	print(solution())