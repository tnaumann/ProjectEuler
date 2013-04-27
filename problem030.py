"""
Project Euler (http://projecteuler.net/)
Problem 30
"""

def maxn(power):
	n = 1
	while n*9**power >= 10**(n-1):
		n += 1
	return n

def solution():
	dig5 = lambda n, power: n == sum(int(s)**power for s in str(n))
	return sum(i for i in range(2, maxn(5)*9**5) if dig5(i,5))

if __name__ == "__main__":
    print(solution())