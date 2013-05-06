"""
Project Euler (http://projecteuler.net/)
Problem 54
"""

from contextlib import closing
from urllib.request import urlopen

URL = 'http://projecteuler.net/project/poker.txt'
with closing(urlopen(URL)) as f:
	CONTENT = f.read().decode()
	
def solution():
	inp = (x.split() for x in CONTENT.strip().split('\n'))
	rounds = ((x[:len(x) // 2], x[len(x) // 2:]) for x in inp)

	value = {
		'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 
		'T':10, 'J':11, 'Q':12, 'K':13, 'A':14
	}
	all_kinds = tuple(reversed(sorted(value.values())))
	all_suits = tuple('SHDC')
	
	def make_hand(cards):
		hand = {}
		for card in cards:
			hand.setdefault(value[card[0]], set()).add(card[1])
			hand.setdefault(card[1], set()).add(value[card[0]])
		return hand
	def get(hand, part): return ((i, hand.get(i, set())) for i in part)
	def has(hand, part): return not sum(1 for i in part if i not in hand)
	
	def rank(hand):
		for suit, kinds in get(hand, all_suits):	# Royal flush
			if has(kinds, tuple('TJQKA')):
				return (9,)

		for suit, kinds in get(hand, all_suits):	# Straight flush
			kinds = sorted(kind for kind in kinds)
			if len(kinds) == 5 and kinds[4] - kinds[0] == 4:
				return (8, kinds[0])
				
		for kind, suits in get(hand, all_kinds):	# Four of a kind
			if len(suits) == 4:
				return (7, kind)
				
		for kind, suits in get(hand, all_kinds):	# Full house
			if len(suits) == 3:
				for kind2, suits2 in get(hand, all_kinds):
					if len(suits2) == 2:
						return (6, kind, kind2)

		for suit, kinds in get(hand, all_suits):	# Flush
			if len(kinds) == 5:
				return (5,)

		kinds = sorted(kind for kind in all_kinds if kind in hand)	# Straight
		if len(kinds) == 5 and kinds[4] - kinds[0] == 4:
			return (4, kinds[0])

		for kind, suits in get(hand, all_kinds):	# Three of a kind
			if len(suits) == 3:
				return (3, kind)

		for kind, suits in get(hand, all_kinds):	# Two pairs
			if len(suits) == 2:
				for kind2, suits2 in get(hand, all_kinds):
					if kind != kind2 and len(suits2) == 2:
						return (2, kind, kind2)

		for kind, suits in get(hand, all_kinds):	# One pair
			if len(suits) == 2:
				return (1, kind)
				
		for kind in all_kinds:	# High card
			if kind in hand:
				return (0, kind)

		return 0

	return sum(1 
		for r in rounds 
		if rank(make_hand(r[0])) > rank(make_hand(r[1]))
	)

if __name__ == "__main__":
    print(solution())