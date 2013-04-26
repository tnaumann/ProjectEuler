"""
Project Euler (http://projecteuler.net/)
Problem 28
"""


def solution():
	# upper right = n*n
	# upper left  = n*n - n + 1
	# lower left  = n*n - 2*n + 2
	# lower right = n*n - 3*n + 3
	# sum         = 4*n*n - 6*n + 	
	return 1 + sum(map(lambda n: 4*n*n - 6*n + 6, range(3,1002,2)))

if __name__ == "__main__":
    print(solution())