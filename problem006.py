"""
Project Euler (http://projecteuler.net/)
Problem 6
"""

def solution():
	sum_of_sq = lambda n: sum(map(lambda x: x**2, range(n+1)))
	sq_of_sum = lambda n: sum(range(n+1))**2
	return sq_of_sum(100) - sum_of_sq(100)

if __name__ == "__main__":
	print(solution())