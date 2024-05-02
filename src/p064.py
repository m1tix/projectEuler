from math import sqrt
from p066 import continued_fraction

def problem(b):
    '''
        Returns the number of irrational square roots 
        that have an odd period.
    '''
    tot = 0
    for d in range(2, b + 1):
        if int(sqrt(d)) == sqrt(d):
            continue
        cont_frac = continued_fraction(d)
        if len(cont_frac) % 2 == 0:
            tot += 1
    return tot

if __name__ == "__main__":
    print(problem(10000))
