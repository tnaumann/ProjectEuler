"""
Project Euler (http://projecteuler.net/)
Problem 16
"""

def solution():
	return sum(int(x) for x in str(2**1000))

if __name__ == "__main__":
	print(solution())