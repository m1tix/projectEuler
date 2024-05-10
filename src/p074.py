from collections import defaultdict
from random import randint
from math import factorial, floor, log10

PRECALC = {str(k) : factorial(k) for k in range(10)}

def next_in_chain(n):
    return sum(PRECALC[k] for k in str(n))

def problem():
    length_dict = defaultdict(int)
    count = 0
    for n in range(1, 50000):
        curr = [n]
        m = n
        while next_in_chain(m) not in curr:
            m = next_in_chain(m)
            curr.append(m)
        repeat_factor = next_in_chain(m)
        if len(curr) == 60:
            count += 1
    print(count)


if __name__ == "__main__":
    print(problem())
