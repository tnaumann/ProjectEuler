"""
Project Euler (http://projecteuler.net/)
Problem 48
"""

def solution():
	return int(str(sum(i**i for i in range(1, 1001)))[-10:])

if __name__ == "__main__":
    print(solution())