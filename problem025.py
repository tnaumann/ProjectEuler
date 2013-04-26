"""
Project Euler (http://projecteuler.net/)
Problem 25
"""

def fibonacci():
	f0, f1 = 1, 1
	while True:
		yield f0
		f0, f1 = f1, f0 + f1

def solution():
	for i,n in enumerate(fibonacci()):
		if len(str(n)) >= 1000:
			break
	return i

if __name__ == "__main__":
    print(solution())