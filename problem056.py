"""
Project Euler (http://projecteuler.net/)
Problem 56
"""

def solution():
	digsum = lambda n: sum(int(c) for c in str(n))
	return max(digsum(a**b) for a in range(100) for b in range(100))

if __name__ == "__main__":
    print(solution())