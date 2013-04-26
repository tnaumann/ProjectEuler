"""
Project Euler (http://projecteuler.net/)
Problem 29
"""

def solution():
	return len({a**b for a in range(2,101) for b in range(2,101)})

if __name__ == "__main__":
    print(solution())