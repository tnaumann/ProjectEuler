"""
Project Euler (http://projecteuler.net/)
Problem 5
"""

from functools import reduce
from itertools import count, takewhile
import operator

def factor(number):
	factors = [(1, 1)]
	
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
	# aggregate the factors
	num = {}
	for e in range(1,21):
		for k,v in factor(e):
			if k not in num:
				num[k] = 0
			num[k] = max(num[k],v)
			
	return reduce(operator.mul, (k**v for k,v in num.items()))

if __name__ == "__main__":
	print(solution())