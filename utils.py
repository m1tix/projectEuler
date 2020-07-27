from math import sqrt, ceil


def sieve_erasosthenes(n):
    # generates primes <= n with sieve of erasosthenes
    primeList = [0]*2 + [1] * (n-1)
    for i in range(ceil(sqrt(n)) + 1):
        if primeList[i]:
            for j in range(i**2, n+1, i):
                primeList[j] = False
    return [i for i, prime in enumerate(primeList) if prime]


def miller_rabin(n):
    '''
        Determines primality of odd n with Miller-Rabin test (the deterministic
        version). If n < 2^64, then the function will correctly give the
        primality of n, see Pomerance "Prime numbers: A computational approach"
        page 139
        It is possible to implement the deterministic Miller-Rabin test for
        larger values of n, although this is not needed for now.
    '''
    bounds = [(2047, (2)),
              (1373653, (2, 3)),
              (9080191, (31, 73)),
              (25326001, (2, 3, 5)),
              (3215031751, (2, 3, 5, 7)),
              (4759123141, (2, 7, 61)),
              (1122004669633, (2, 13, 23, 1662803)),
              (2152302898747, (2, 3, 5, 7, 11)),
              (3474749660383, (2, 3, 5, 7, 11, 13)),
              (341550071728321, (2, 3, 5, 7, 11, 13, 17)),
              (3825123056546413051, (2, 3, 5, 7, 11, 13, 17, 19, 23)),
              (2**64, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37))]
    if n in (2, 3):
        return 1
    if n % 2 == 0:
        return 0
    # determine integers r and d such that n = 2^r * d + 1
    r, d = 0, n-1
    while d % 2 == 0:
        r += 1
        d = d >> 1

    # Function to determine if a number is composite. If false, then it is not
    # certain that the number is prime.
    def composite(a, n, r, d):
        x = pow(a, d, n)
        if x == 1:
            return False
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                return False
        return True

    for m in bounds:
        if n < m[0]:
            return not any(composite(a, n, r, d) for a in m[1])


print(miller_rabin(13103))
