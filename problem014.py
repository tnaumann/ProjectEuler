"""
Project Euler (http://projecteuler.net/)
Problem 14
"""

from functools import wraps

def memo(f):
	cache = {}
	@wraps(f)
	def wrapper(*args):
		if args not in cache:
			cache[args] = f(*args)
		return cache[args]
	return wrapper

@memo
def collatz_len(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + collatz_len(n/2)
    return 1 + collatz_len(3*n + 1)

def solution():
	return max(range(1,1000000), key=collatz_len)

if __name__ == "__main__":
	print(solution())