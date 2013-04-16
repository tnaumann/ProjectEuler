"""
Project Euler (http://projecteuler.net/)
Problem 3
"""

from itertools import count, takewhile

def solution():
	number = 600851475143

	primes = [2]
	while primes[-1] < number:
		# divide
		while number % primes[-1] == 0:
			number //= primes[-1]

		# next prime
		for i in count(primes[-1] + 1):
			lte_sqrt = lambda p: p*p <= i
			if not any(i % j == 0 for j in takewhile(lte_sqrt, primes)):
				primes.append(i)
				break
		
	return primes[-1]

if __name__ == "__main__":
	print(solution())