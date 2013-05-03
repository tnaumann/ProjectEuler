"""
Project Euler (http://projecteuler.net/)
Problem 51
"""

from collections import defaultdict
from itertools import count

def solution():
	D = defaultdict(list)
	primes = []
	def add_prime():
		init = primes and primes[-1] + 1 or 2
		for q in count(init):
			if q not in D:
				D[q * q] += [q]
				primes.append(q)
				break
			else:
				for p in D[q]:
					D[p + q] += [p]
				del D[q]
				
	def count_primes():
		for i in count():
			while i >= len(primes):
				add_prime()
			yield primes[i]
			
	def is_prime(n):
		while n > primes[-1]:
			add_prime()
		return n in primes
	
	for p in count_primes():
		s = str(p)
		alts = lambda s, r: (s.replace(r, d) for d in '0123456789')
		flen = lambda s, r: sum(1 for x in alts(s, r) if x[0] != '0' and is_prime(int(x)))
		
		if any(s.count(d) == 3 and flen(s, d) >= 8 for d in '012'):
			return p

if __name__ == "__main__":
    print(solution())