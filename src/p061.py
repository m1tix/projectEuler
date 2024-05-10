from itertools import permutations
from math import ceil, floor, sqrt


def s_gonal(s, n):
    '''
        Return the n-th s-gonal, s >= 2,  number
    '''
    return ((s - 2) * n ** 2 - (s - 4) * n) // 2

def old_problem(gonals):
    '''
        Return a list of tuples, each of len(gonals) length, such that for
        each tuple we have:
            i) every element is unique and consists of 4 digits;
            ii) The i-th element is s-gonal for some unique s in gonals;
            iii) The last two digits of the i-th element are precisely
                the first two digits of the (i + 1)-th element (wrapping around to 0).

        Assumes that gonals is of at least length 2 and contains only integers larger than 2.

        Some observations:
            - If P(s, n) denotes the n-th s-gonal number, then

                P(s, n) = ((s - 2) n^2 - (s - 4)n) / 2
    '''
    tot = []
    for perm_gonals in permutations(gonals, len(gonals)):
        res = [[s_gonal(perm_gonals[0], n)] for n in range(1, 1000) if 1000 <= s_gonal(perm_gonals[0], n) <= 9999]
        for i, s in enumerate(perm_gonals[1:]):
            lower_bound = ceil(sqrt(2000 / (s - 2) + (s - 4) ** 2 / (4 * (s - 2) ** 2)) + (s - 4) / (2 * s - 4))
            upper_bound = floor(sqrt(19998 / (s - 2) + (s - 4) ** 2 / (4 * (s - 2) ** 2)) + (s - 4) / (2 * s - 4))
            curr = []
            for prev in res:
                for n in range(lower_bound, upper_bound + 1):
                    gon = s_gonal(s, n)
                    wrap_condition = True
                    if i == len(perm_gonals) - 2:
                        wrap_condition = str(prev[0])[:2] == str(gon)[2:]
                    if str(prev[-1])[2:] == str(gon)[:2] and wrap_condition:
                        curr.append(prev + [gon])
            res = curr
            if i == len(perm_gonals) - 2 and res:
                tot += res
    return tot

def fits_in(l, n):
    '''
        Returns True together with an index i if the number n satisfies the conditions of the problem at index i.
        That is
            The last two digits of (i-1)-th element are the first two digits of n
            The last two digits of n are the first two digits of the i-th element.
        NO WRAPPING and only works with 4 digits numbers
    '''
    fits = []
    for i in range(len(l) + 1):
        if i == 0:
            cond = str(l[i])[:2] == str(n)[2:]
        elif i == len(l):
            cond = str(l[i - 1])[2:] == str(n)[:2]
        else:
            cond = (str(l[i - 1])[2:] == str(n)[:2] and
                    str(l[i])[:2] == str(n)[2:])
        if cond:
            fits.append(i)
    return fits


def problem(gonals):
    '''
        Return a list of tuples, each of len(gonals) length, such that for
        each tuple we have:
            i) every element is unique and consists of 4 digits;
            ii) The i-th element is s-gonal for some unique s in gonals;
            iii) The last two digits of the i-th element are precisely
                the first two digits of the (i + 1)-th element (wrapping around to 0).

        Assumes that gonals is of at least length 2 and contains only integers larger than 2.
        Is much faster than old_problem, but does not work in all HackerRank tests....

        Some observations:
            - If P(s, n) denotes the n-th s-gonal number, then

                P(s, n) = ((s - 2) n^2 - (s - 4)n) / 2

    '''
    res = [[s_gonal(gonals[0], n)] for n in range(1, 1000) if 1000 <= s_gonal(gonals[0], n) <= 9999]
    # Basically: loop over all previously found list and all (valid) s-gonal numbers
    # to check whether the s-gonal number fits in the list. If so, add them to the list
    # in all possible spots and repeat till done
    for s in gonals[1:]:
        lower_bound = ceil(sqrt(2000 / (s - 2) + (s - 4) ** 2 / (4 * (s - 2) ** 2)) + (s - 4) / (2 * s - 4))
        upper_bound = floor(sqrt(19998 / (s - 2) + (s - 4) ** 2 / (4 * (s - 2) ** 2)) + (s - 4) / (2 * s - 4))
        curr = []
        for prev in res:
            for n in range(lower_bound, upper_bound + 1):
                gon = s_gonal(s, n)
                indices = fits_in(prev, gon)
                if indices:
                    curr += [prev[:i] + [gon] + prev[i:] for i in indices]
            res = curr
    # In the end, make sure that the wrapping condition holds.
    return list(filter(lambda x: str(x[0])[:2] == str(x[-1])[2:], res))

if __name__ == "__main__":
    print(old_problem([3,4,5,6,7]))
    # BUG WHEN MULTIPLE OF SAME GON
