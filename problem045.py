"""
Project Euler (http://projecteuler.net/)
Problem 45
"""

from itertools import count

def solution():
	# all hex numbers are triangle numbers so find next hex that's penta
	for n in count(144):
		h = n * (2*n - 1)
		k = (1 + (1 + 24*h)**0.5) / 6
		if k == int(k):
			return h

if __name__ == "__main__":
    print(solution())