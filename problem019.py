"""
Project Euler (http://projecteuler.net/)
Problem 19
"""

from datetime import datetime

def solution():
	return sum(1 
		for m in range(1,13) 
		for y in range(1901,2001) 
		if datetime(y, m, 1).weekday() == 6
	)

if __name__ == "__main__":
    print(solution())