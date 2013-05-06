"""
Project Euler (http://projecteuler.net/)
Problem 58
"""

def solution():
	def is_prime(n):
		if n == 2 or n == 3: return True
		if n < 2 or n % 2 == 0: return False
		if n < 9: return True
		if n % 3 == 0: return False
		f = 5
		while f * f <= n:
			if n % f == 0: return False
			if n % (f+2) == 0: return False
			f += 6
		return True
		
	np, d, avg, n = 0, 1, 1, 2
	while avg >= 0.10:
		np += sum(1 for i in range(3) if is_prime(d + (i+1)*n))
		d += 4*n
		n += 2
		avg = np / (2*n)
		
	return n - 1

if __name__ == "__main__":
    print(solution())