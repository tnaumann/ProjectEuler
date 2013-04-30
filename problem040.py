"""
Project Euler (http://projecteuler.net/)
Problem 40
"""

from functools import reduce
import operator

def solution():
	s = ''.join([str(x) for x in range(200000)])
	prod = lambda x: reduce(operator.mul, x)
	return prod(int(s[10**i]) for i in range(7))

if __name__ == "__main__":
    print(solution())