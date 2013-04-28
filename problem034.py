"""
Project Euler (http://projecteuler.net/)
Problem 34
"""

from math import factorial

def solution():
	lim = factorial(9) * 7
	return sum(i for i in range(3,lim) 
		if i == sum(factorial(int(j)) for j in str(i))
	)

if __name__ == "__main__":
    print(solution())