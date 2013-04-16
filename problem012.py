"""
Project Euler (http://projecteuler.net/)
Problem 12
"""

from functools import reduce
from itertools import count, takewhile
import operator

def factor(number):
	factors = [(1,1)]
	
	if number == 1:
		return factors
	
	primes = [2]
	while primes[-1] <= number:
		# divide
		pcount = 0
		while number % primes[-1] == 0:
			number //= primes[-1]
			pcount += 1
		factors += [(primes[-1], pcount)]
			
		# next prime
		for i in count(primes[-1] + 1):
			lte_sqrt = lambda p: p*p <= i
			if not any(i % j == 0 for j in takewhile(lte_sqrt, primes)):
				primes.append(i)
				break
				
	return factors

def solution():
	numfact = lambda x: reduce(operator.mul, (c+1 for _,c in factor(x)[1:]))

	i = 2
	trinum = 3
	while numfact(trinum) <= 500:
		i += 1
		trinum += i

	return trinum

if __name__ == "__main__":
	print(solution())