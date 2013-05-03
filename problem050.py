"""
Project Euler (http://projecteuler.net/)
Problem 50
"""

from itertools import takewhile

def solution():
	primes = [2]
	cumsum = [2]	# running sum speed up later search
	for i in range(3, 1000000, 2):
		lte_sqrt = lambda p: p*p <= i
		if not any(i % j == 0 for j in takewhile(lte_sqrt, primes)):
			primes.append(i)
			if cumsum[-1] < 1000000:
				cumsum.append(cumsum[-1] + i)
	
	terms = 1
	for i in range(len(cumsum)):
		for j in range(i+terms, len(cumsum)):
			d = cumsum[j] - cumsum[i]
			if d in primes:
				terms, max_prime = j-i, d
				
	return max_prime

if __name__ == "__main__":
    print(solution())