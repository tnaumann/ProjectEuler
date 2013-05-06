"""
Project Euler (http://projecteuler.net/)
Problem 57
"""

def solution():
	def series():
		n, d = 3, 2
		for i in range(2, 1000):
			n, d = n + 2*d, n + d
			yield n, d
			
	return sum(1 for n, d in series() if len(str(n)) > len(str(d)))

if __name__ == "__main__":
    print(solution())