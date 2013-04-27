"""
Project Euler (http://projecteuler.net/)
Problem 31
"""

def solution():
	# Count down from the top to avoid recursion
	return sum(1
		for a in range(200, -1, -200)
		for b in range(a, -1, -100)
		for c in range(b, -1, -50)
		for d in range(c, -1, -20)
		for e in range(d, -1, -10)
		for f in range(e, -1, -5)
		for g in range(f, -1, -2)
	)

if __name__ == "__main__":
    print(solution())