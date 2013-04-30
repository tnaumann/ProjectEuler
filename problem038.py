"""
Project Euler (http://projecteuler.net/)
Problem 38
"""

from itertools import count

def ispandi(n):
	digs = str(n)
	for i in count(2):
		if len(digs) < 9:
			digs += str(n*i)
		elif len(digs) == 9 and set(digs) == set('123456789'):
			return int(digs)
		else:
			return False

def solution():
	return max(map(ispandi, range(1,10000)))

if __name__ == "__main__":
    print(solution())