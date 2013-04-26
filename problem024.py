"""
Project Euler (http://projecteuler.net/)
Problem 24
"""

from math import factorial

def permn(s, n):
		if len(s) == 1:
			return s
		c = factorial(len(s)-1)
		i = n // c
		return s[i] + permn(s[:i] + s[i+1:], n - i*c)

def solution():
	return int(permn('0123456789', 999999))

if __name__ == "__main__":
    print(solution())