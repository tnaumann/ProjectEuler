"""
Project Euler (http://projecteuler.net/)
Problem 36
"""
	
def solution():
	isPal = lambda x: x == x[::-1]

	return sum(i 
		for i in range(1,1000000,2) 
		if isPal(str(i)) and isPal(bin(i)[2:])
	)

if __name__ == "__main__":
    print(solution())