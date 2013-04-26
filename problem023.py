"""
Project Euler (http://projecteuler.net/)
Problem 23
"""

from itertools import chain

def solution():
	divisors = lambda n: chain.from_iterable({i, n // i} 
		for i in range(2, int(n**0.5) + 1) if n % i == 0
	)
	d = lambda n: 1 + sum(divisors(n))

	abundants = {i for i in range(1,28124) if d(i) > i}
	asum = lambda n: any(n-a in abundants for a in abundants)

	return sum(i for i in range(1,28124) if not asum(i))

if __name__ == "__main__":
    print(solution())