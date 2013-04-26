"""
Project Euler (http://projecteuler.net/)
Problem 22
"""

from contextlib import closing
from urllib.request import urlopen

URL = 'http://projecteuler.net/project/names.txt'
with closing(urlopen(URL)) as f:
	CONTENT = f.read().decode()

def solution():
	names = sorted(x.strip('"') for x in CONTENT.split(','))
	wordval = lambda w: sum(ord(c)-64 for c in w)

	return sum(i * wordval(n) for i,n in enumerate(names, 1))

if __name__ == "__main__":
    print(solution())