"""
Project Euler (http://projecteuler.net/)
Problem 2 
"""

from itertools import takewhile

def fibonacci():
	f0, f1 = 1, 2
	while True:
		yield f0
		f0, f1 = f1, f0 + f1

def solution():
	upto4000000 = takewhile(lambda x: x <= 4000000, fibonacci())
	return sum(filter(lambda x: x % 2 == 0, upto4000000))

if __name__ == "__main__":
	print(solution())