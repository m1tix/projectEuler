from math import sqrt, ceil, prod
import timeit


def sieve_eratosthenes(n):
    # generates primes <= n with sieve of erasosthenes
    primeList = [0]*2 + [1] * (n-1)
    for i in range(ceil(sqrt(n)) + 1):
        if primeList[i]:
            for j in range(i**2, n+1, i):
                primeList[j] = 0
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
    bounds = [(2047, (2,)),
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

    def composite(a, n, r, d):
        '''
            Function to determine if a number is composite. If true, then the
            number is certainly prime, but if false the number need not be
            prime.
            The function works because if n = 2^r * d + 1 is prime, then for
            all numbers a relatively prime to n we have

              a^(2^r*d) - 1 = (a^d - 1)(a^(2d) + 1)...(a^(2^r*d) + 1) = 0 mod n

            hence the validity of the function.
        '''
        x = pow(a, d, n)
        if x in (1, n - 1):
            return False
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                return False
        return True

    for m in bounds:
        if n < m[0]:
            return not any(composite(a, n, r, d) for a in m[1])


def factor(n):
    '''
        Returns the factors of n in a list of tuples with exponents.
        Uses sieve of eratosthenes to generate primes, so only useful for,
        rougly speaking, small numbers. Should use ECM for larger numbers.
        Can possibly be optimized by first storing a few small primes to test
        and possibly lower n.
    '''
    factors = []
    possiblePrimes = sieve_eratosthenes(ceil(sqrt(n)))
    for prime in possiblePrimes:
        exp = 0
        while n % prime == 0:
            exp += 1
            n = n // prime
        if exp != 0:
            factors.append((prime, exp))
    if n != 1:
        return factors + [(n, 1)]
    return factors


def number_divisors(n):
    '''
        Returns the number of divisors of n
    '''
    factors = factor(n)
    return prod(k[1] + 1 for k in factors)


def sum_divisors(n):
    '''
        Returns the sum of the proper divisors of n.
    '''
    factors = factor(n)
    return prod((p**(e+1) - 1) // (p-1) for p, e in factors) - n


def is_perfect(n):
    '''
        Returns True when n is perfect and False otherwise. A number n is
        perfect when sum_divisors(n) == n
    '''
    return sum_divisors(n) == n


def is_deficient(n):
    '''
        Returns True if n is deficient and False otherwise. A number k is
        deficient when sum_divisors(k) < k
    '''
    return sum_divisors(n) < n


def is_abundant(n):
    '''
        Returns True if n is abundant and False otherwise. A number k is
        abundant when sum_divisors(k) > k, i.e. it is not perfect nor deficient
    '''
    return sum_divisors(n) > n


def generate_abundant(n):
    '''
        Returns a list where the i-th entry is True when i is abundant and
        False otherwise, i.e. it generates all the abundant numbers up to n
    '''
    abundantNumbers = [0]*(n+1)
    for k in range(2, n+1):
        if not abundantNumbers[k] and is_abundant(k):
            for i in range(k, n + 1, k):
                abundantNumbers[i] = 1
    return abundantNumbers


if __name__ == "__main__":
    setup1 = "from __main__ import generate_abundant"
    print(timeit.timeit("generate_abundant(10**5)", setup=setup1, number=1))
