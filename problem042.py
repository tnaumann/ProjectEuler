"""
Project Euler (http://projecteuler.net/)
Problem 42
"""

from contextlib import closing
from urllib.request import urlopen

URL = 'http://projecteuler.net/project/words.txt'
with closing(urlopen(URL)) as f:
	CONTENT = f.read().decode()

def solution():
	inp = [x.strip('"') for x in CONTENT.split(',')]

	wordval = lambda w: sum(ord(c)-64 for c in w)
	wordvals = map(wordval, inp)

	triind = lambda x: (1 + 8*x)**0.5 - 1
	triinds = map(triind, wordvals)

	return sum(1 for e in triinds if e == int(e))

if __name__ == "__main__":
    print(solution())