"""
Project Euler (http://projecteuler.net/)
Problem 33
"""

from functools import reduce
import operator

def solution():
	prod = lambda x: reduce(operator.mul, x)
	fracs = ((10*y + z)/(10*x + y)
		for x in range(1, 10)
		for y in range(1, 10)
		for z in range(1, 10)
		if 10*x + y != 10*y + z and 9*x*z + y*z == 10*x*y
	)

	return int(prod(fracs))

if __name__ == "__main__":
    print(solution())