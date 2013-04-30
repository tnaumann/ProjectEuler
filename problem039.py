"""
Project Euler (http://projecteuler.net/)
Problem 39
"""

def nfound(p):
    return len([(a,b,(a*a + b*b)**0.5)
               for a in range(1, p // 4 + 1)
               for b in range(a+1, (p-a) // 2 + 1)
               if a + b + (a*a + b*b)**0.5 == p
               ])

def solution():
	return max(range(1,1000), key=nfound)

if __name__ == "__main__":
    print(solution())