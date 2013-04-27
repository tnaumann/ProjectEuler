"""
Project Euler (http://projecteuler.net/)
Problem 32
"""

def solution():
	possa = [10*a + b for a in range(10) for b in range(10) if a != b]
	possb = [b for b in range(100, 9999) if len(str(b)) == len(set(str(b)))]

	sol = set()
	for a in possa:  
		for b in possb:
			if b < max(a,1000.0 / a): continue
			if b > 9999.0 / a: break        
			c = a*b
			if "".join(sorted(str(a)+str(b)+str(c))) == "123456789":            
				sol.add(c)
	return sum(sol)

if __name__ == "__main__":
    print(solution())