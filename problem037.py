"""
Project Euler (http://projecteuler.net/)
Problem 37
"""

from itertools import count

def isp(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5+1), 2):
        if n % i == 0: return False
    return True

def istrunc(n):
    for i in range(len(str(n))-1):
        if not isp(int(str(n)[:i+1])): return False
        if not isp(int(str(n)[i+1:])): return False
    return True

def solution():
    tprimes = []
    for i in count(11, 2):
        if isp(i) and istrunc(i):
            tprimes.append(i)

        if len(tprimes) >= 11:
            break
		
    return sum(tprimes)

if __name__ == "__main__":
    print(solution())