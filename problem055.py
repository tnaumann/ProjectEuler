"""
Project Euler (http://projecteuler.net/)
Problem 55
"""

def solution():
	isPal = lambda n: str(n) == str(n)[::-1]

	def is_lychrel(n):
		for i in range(50):
			n = n + int(str(n)[::-1])
			if isPal(n): return False
		return True
		
	return sum(is_lychrel(n) for n in range(10000))

if __name__ == "__main__":
    print(solution())