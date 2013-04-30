"""
Project Euler (http://projecteuler.net/)
Problem 41
"""

from itertools import permutations

def isp(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5+1), 2):
        if n % i == 0: return False
    return True

def solution():
	pandigitals = (int(''.join(map(str, p)))
		for n in range(9, 0, -1)
		for p in permutations(range(n, 0, -1))
	)

	return next(p for p in pandigitals if isp(p))

if __name__ == "__main__":
    print(solution())