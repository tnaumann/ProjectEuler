"""
Project Euler (http://projecteuler.net/)
Problem 35
"""

from itertools import groupby, takewhile


def solution():
	primes = [2]
	for i in range(3, 1000000, 2):
		lte_sqrt = lambda p: p*p <= i
		if not any(i % j == 0 for j in takewhile(lte_sqrt, primes)):
			primes.append(i)

	rotations = lambda s: (s[i:] + s[:i] for i in range(len(s)))
	keyfunc = lambda s: sorted(rotations(str(s)))[0]
	candidates = sorted(primes, key=keyfunc)
	groups = ((k, list(g)) for k, g in groupby(candidates, keyfunc))

	return sum(len(g)
		for k, g in groups
		if len(k) == len(g)
		or all(i == k[0] for i in k)
	)

if __name__ == "__main__":
    print(solution())