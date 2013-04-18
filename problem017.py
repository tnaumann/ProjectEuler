"""
Project Euler (http://projecteuler.net/)
Problem 17
"""

digs = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = [None, None, 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def written(n):
    n, o = divmod(n, 10)
    n, t = divmod(n, 10)
    n, h = divmod(n, 10)
    n, r = divmod(n, 10)

    word = ''
    if t == 1:
        word = teens[o] + word
    else:
        if o:
            word = digs[o] + word
        if t:
            word = tens[t] + word

    if h:
        if t or o:
            word = 'and' + word
        word = 'hundred' + word
        word = digs[h] + word

    if r:
        word = 'thousand' + word
        word = digs[r] + word
    return word

def solution():
    written_len = lambda i: len(written(i))
    return sum(map(written_len, range(1,1001)))

if __name__ == "__main__":
    print(solution())