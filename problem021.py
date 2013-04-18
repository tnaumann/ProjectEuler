"""
Project Euler (http://projecteuler.net/)
Problem 21
"""

from itertools import chain

def solution():
	divisors = lambda n: chain.from_iterable({i, n // i} 
		for i in range(2, int(n**0.5) + 1) if n % i == 0
	)
	d = lambda n: 1 + sum(divisors(n))
	return sum(i for i in range(1,10000) if d(d(i)) == i and i != d(i))

if __name__ == "__main__":
    print(solution())