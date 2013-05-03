"""
Project Euler (http://projecteuler.net/)
Problem 52
"""

from itertools import count

def solution():
	for i in count(1):
		digits = lambda n: sorted(str(n))
		if all(digits(i) == digits(a*i) for a in range(2,7)):
			   return i

if __name__ == "__main__":
    print(solution())