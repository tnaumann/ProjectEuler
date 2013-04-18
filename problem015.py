"""
Project Euler (http://projecteuler.net/)
Problem 15
"""

from math import factorial

def solution():
	return int(factorial(20 + 20) / factorial(20)**2)

if __name__ == "__main__":
	print(solution())