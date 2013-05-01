"""
Project Euler (http://projecteuler.net/)
Problem 47
"""

from collections import defaultdict
from itertools import count

def solution():
	t = 0
	D = defaultdict(list)	# Map to prime witnesses
	for q in count(2):
		if q not in D:
			t = 0
			D[2 * q] += [q]
		else:
			if len(D[q]) == 4:
				t += 1
			else:
				t = 0

			if t == 4:
				return q - 3

			for p in D[q]:
				D[p + q] += [p]
			del D[q]

if __name__ == "__main__":
    print(solution())