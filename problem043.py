"""
Project Euler (http://projecteuler.net/)
Problem 43
"""

def solution():
	primes = [2, 3, 5, 7, 11, 13, 17]
	prop = lambda s: all(int(s[i+1:i+4]) % primes[i] == 0 
		for i in reversed(range(len(primes)))
	)

	poss = (d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10
		for d1 in set('123456789')	# can't start with 0
		for d2 in set('0123456789') - {d1}
		for d3 in set('0123456789') - {d1, d2}
		for d4 in set('02468') - {d1, d2, d3}	# divisible by 2
		for d5 in set('0123456789') - {d1, d2, d3, d4}
		for d6 in set('05') - {d1, d2, d3, d4, d5}	# divisible by 5
		for d7 in set('0123456789') - {d1, d2, d3, d4, d5, d6}
		for d8 in set('0123456789') - {d1, d2, d3, d4, d5, d6, d7}
		for d9 in set('0123456789') - {d1, d2, d3, d4, d5, d6, d7, d8}
		for d10 in set('0123456789') - {d1, d2, d3, d4, d5, d6, d7, d8, d9}
	)

	return sum(int(v) for v in poss if prop(v))

if __name__ == "__main__":
    print(solution())