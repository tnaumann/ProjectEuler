"""
Project Euler (http://projecteuler.net/)
Problem 7
"""

from itertools import count, takewhile

def solution():
	primes = [2]
	while len(primes) < 10001:
		# next prime
		for i in count(primes[-1] + 1):
			lte_sqrt = lambda p: p*p <= i
			if not any(i % j == 0 for j in takewhile(lte_sqrt, primes)):
				primes.append(i)
				break
				
	return primes[-1]

if __name__ == "__main__":
	print(solution())