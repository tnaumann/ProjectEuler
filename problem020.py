"""
Project Euler (http://projecteuler.net/)
Problem 20
"""

from math import factorial

def solution():
	digit_sum = lambda n: sum(int(d) for d in str(n))
	return digit_sum(factorial(100))

if __name__ == "__main__":
    print(solution())