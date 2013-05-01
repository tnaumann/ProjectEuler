"""
Project Euler (http://projecteuler.net/)
Problem 44
"""

from itertools import count

def solution():
	pentas = set()
	pdiffs = {}

	for n in count(1):
		p = n * (3*n - 1) // 2 #p += 3*n + 1

		if p in pdiffs:
			return pdiffs[p]

		for old in pentas:
			diff = p - old
			if diff in pentas:
				pdiffs[p+old] = diff
		pentas.add(p)

if __name__ == "__main__":
    print(solution())