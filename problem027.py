"""
Project Euler (http://projecteuler.net/)
Problem 27
"""

from itertools import takewhile

def solution():
	primes = [2]
	for i in range(3, 10000, 2):
		lte_sqrt = lambda p: p*p <= i
		if not any(i % j == 0 for j in takewhile(lte_sqrt, primes)):
			primes.append(i)

	isprime = lambda n: n in primes
		
	def quadplen(a,b):
		n = 0
		while n*n + a*n + b in primes:
			n += 1
		return n
		
	primeb = filter(isprime, range(1001))
	ma = 0
	mb = 0
	m = 0
	for b in primeb:
		for a in range(-b, 1000):
			n = quadplen(a, b)
			if n > m:
				m, ma, mb = n, a, b
	return ma*mb

if __name__ == "__main__":
    print(solution())