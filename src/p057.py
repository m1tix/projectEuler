from math import log10, floor

from p066 import continued_fraction

def problem(b, d):
    '''
        Returns the number of n-th convergents (n <= b) of sqrt(d) such that
        the numerator has more digits then the denominator.
    '''
    # stolen from p066, but still made it modular
    cont_frac = continued_fraction(d)
    p_prev, p_new = 1, cont_frac[0]
    q_prev, q_new = 0, 1
    period = len(cont_frac) - 1
    tot = 0
    for i in range(0, b):
        ai = cont_frac[1 + (i % period)]
        p_prev, p_new = p_new, ai * p_new + p_prev
        q_prev, q_new = q_new, ai * q_new + q_prev
        if floor(log10(p_new)) > floor(log10(q_new)):
            tot += 1
    return tot

if __name__ == "__main__":
    print(problem(10 ** 4,2))
