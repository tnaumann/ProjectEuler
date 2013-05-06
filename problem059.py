"""
Project Euler (http://projecteuler.net/)
Problem 59
"""

from contextlib import closing
import contextlib
from itertools import cycle, product
import operator
import re
import string
from urllib.request import urlopen

URL = 'http://projecteuler.net/project/cipher1.txt'
with closing(urlopen(URL)) as f:
	CONTENT = f.read().decode()


def solution():
	inp = [int(x) for x in CONTENT.strip().split(',')]

	for k in product(string.ascii_lowercase, repeat=3):
		k = map(ord, k)
		msg = map(operator.xor, inp, cycle(k))
		msg = ''.join(map(chr, msg))
		if ' the ' in msg:
			return sum(map(ord, msg))

if __name__ == "__main__":
    print(solution())