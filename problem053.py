"""
Project Euler (http://projecteuler.net/)
Problem 53
"""

from math import factorial

def solution():
	nCr = lambda n, r: factorial(n) / (factorial(r) * factorial(n - r))
	return sum(1 
		for n in range(1, 101) 
		for r in range(n+1) 
		if nCr(n,r) > 10**6
	)

if __name__ == "__main__":
    print(solution())