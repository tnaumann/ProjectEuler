"""
Project Euler (http://projecteuler.net/)
Problem 46
"""

from itertools import count, takewhile
from math import sqrt

def solution():
	primes = [2]
	for i in count(3, 2):
		lte_sqrt = lambda p: p*p <= i
		if not any(i % j == 0 for j in takewhile(lte_sqrt, primes)):
			primes.append(i)
		else:
			diffs = ((i - p) / 2 for p in primes)
			sqrts = map(sqrt, diffs)
			if not any(d == int(d) for d in sqrts):
				return i

if __name__ == "__main__":
    print(solution())