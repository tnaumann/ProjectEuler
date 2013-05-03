"""
Project Euler (http://projecteuler.net/)
Problem 49
"""

from itertools import groupby, takewhile

def solution():
	primes = [2]
	for i in range(3,10000,2):
		lte_sqrt = lambda p: p*p <= i
		if not any(i % j == 0 for j in takewhile(lte_sqrt, primes)):
			primes.append(i)

	pkey = lambda n: ''.join(sorted(str(n)))
	candidates = sorted(primes, key=pkey)
	pd = {k: list(g) for k, g in groupby(candidates, pkey)}

	for i, pi in enumerate(primes):
		if pi < 1000 or pi == 1487: continue

		spi = pkey(pi)
		pals = pd[spi]
		if len(pals) < 3: continue

		for pj in pals:
			if pj <= pi: continue

			diff = pj - pi
			pk = pj + diff

			if pk in pals:
				return int(str(pi) + str(pj) + str(pk))

if __name__ == "__main__":
    print(solution())