"""
Project Euler (http://projecteuler.net/)
Problem 1 
"""

def solution():
	sum_to = lambda n: n * (n + 1) // 2
	return 3 * sum_to(999//3) + 5 * sum_to(999//5) - 15 * sum_to(999//15)

if __name__ == "__main__":
	print(solution())