"""
Project Euler (http://projecteuler.net/)
Problem 26
"""

from itertools import count

def rlen(n):
    r = 10
    seen = {}
    for i in count():
        if r == 0:
            return 0
        if r in seen:
            return i - seen[r]
        seen[r] = i
        r = 10 * (r % n)
		
def solution():
	return max(range(2,1000), key=rlen)

if __name__ == "__main__":
    print(solution())