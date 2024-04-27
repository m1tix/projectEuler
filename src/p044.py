from math import sqrt


def is_pentagonal(n):
    '''
        Returns true if n is pentagonal
    '''
    t = (sqrt(24 * n + 1) + 1) / 6
    # kinda lazy
    # can also do sqrt(24 * n + 1) in Z and sqrt(24 * n + 1) = 5 mod 6.
    return t == int(t)


def pentagonal_numbers():
    '''
        Returns a generator to generate all pentagonal numbers. Works since
            P_{n+1} - P_n = 3 * n + 1
    '''
    p = 1
    n = 1
    while True:
        yield p
        p += 3 * n + 1
        n += 1


def problem():
    '''
        Returns the smallest pair of pentagonal numbers (pn, pm)
        such that
            pn + pm     and     pn - pm
        are both pentagonal. Note that this does not mean that pn - pm
        is minimized (too lazy). Nonetheless, kind of an inefficient method,
        but all other methods seems to be as inefficient. For example,
        another possible approach is to reduce the problem to a sum of two
        squares problem, but then one would need to factor. In SageMath this
        approach seems to be a little faster:
            bound = 5000 # arbitrary
            for k in range(1, bound):
                a, b = sum_of_k_squares(2, 2 * (6 * k - 1) ** 2)
                    if a % 6 == 5 and b % 6 == 5:
                        t = sqrt((6 * k - 1) ** 2 - a ** 2 + 1)
                        if t in ZZ and t % 6 == 5:
                            print((a ** 2 - 1) / 24)
    '''
    for pn in pentagonal_numbers():
        for pm in pentagonal_numbers():
            if pm >= pn:
                break
            if is_pentagonal(pn - pm) and is_pentagonal(pn + pm):
                return pn, pm


def problem_hackerrank(b, k):
    '''
        Returns all pentagonal numbers Pn with n < b such that
        P_n - P_{n-k} or P_n + P_{n-k} is pentagonal
    '''
    res = []
    for n in range(k + 1, b):
        pn = n * (3 * n - 1) // 2
        pk = (n - k) * (3 * (n - k) - 1) // 2
        if is_pentagonal(pn + pk) or is_pentagonal(pn - pk):
            res.append(pn)
    return res

if __name__ == "__main__":
    print(problem())
