from collections import defaultdict
from math import ceil, prod, sqrt

# TODO
## Split this file into multiple files:
### gens.py and primes.py (example)
## Add is_prime with various methods
## Add factor with various methods
## Add euler_phi


def sieve_eratosthenes(n):
    '''
        Generates all primes <= n with a simple sieve
    '''
    prime_list = [0] * 2 + [1] * (n - 1)
    for i in range(ceil(sqrt(n)) + 1):
        if prime_list[i]:
            for j in range(i**2, n + 1, i):
                prime_list[j] = 0
    return [i for i, prime in enumerate(prime_list) if prime]


def sieve_eratosthenes_raw(n):
    '''
        Generates all primes <= n with a simple sieve, but returns a list L
        whose i-th index is 1 iff i is prime.
    '''
    prime_list = [0] * 2 + [1] * (n - 1)
    for i in range(ceil(sqrt(n)) + 1):
        if prime_list[i]:
            for j in range(i**2, n + 1, i):
                prime_list[j] = 0
    return prime_list


def miller_rabin(n):
    '''
        Determines primality of odd n with Miller-Rabin test (the deterministic
        version). If n < 2^64, then the function will correctly give the
        primality of n, see Pomerance "Prime numbers: A computational approach"
        page 139
        It is possible to implement the deterministic Miller-Rabin test for
        larger values of n, although this is not needed for now.
    '''
    bounds = [(2047, (2, )), (1373653, (2, 3)), (9080191, (31, 73)),
              (25326001, (2, 3, 5)), (3215031751, (2, 3, 5, 7)),
              (4759123141, (2, 7, 61)), (1122004669633, (2, 13, 23, 1662803)),
              (2152302898747, (2, 3, 5, 7, 11)),
              (3474749660383, (2, 3, 5, 7, 11, 13)),
              (341550071728321, (2, 3, 5, 7, 11, 13, 17)),
              (3825123056546413051, (2, 3, 5, 7, 11, 13, 17, 19, 23)),
              (2**64, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37))]
    if n in (2, 3):
        return 1
    if n % 2 == 0 or n == 1:
        return 0
    # determine integers r and d such that n = 2^r * d + 1
    r, d = 0, n - 1
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
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True

    for m in bounds:
        if n < m[0]:
            return not any(composite(a, n, r, d) for a in m[1])


def extended_euclidian(a, b):
    '''
        Given two integers a and b return (n,m,d) such that
            an + bm = d,
        with d = gcd(a,b). See Cohen's book 'A course in computational
        algebraic number theory' p. 16.
    '''
    n, d = 1, a
    if b == 0:
        return (n, 0, d)
    m = [0, b]
    while m[1] != 0:
        q = d // m[1]
        t = [n - q * m[0], d % m[1]]
        n, d = m
        m = t
    return (n, (d - a * n) // b, d)


def factor(n):
    '''
        Returns the factors of n in a list of tuples with exponents.
        Uses sieve of eratosthenes to generate primes, so only useful for,
        rougly speaking, small numbers. Should use ECM for larger numbers.
        Can possibly be optimized by first storing a few small primes to test
        and lower n.
    '''
    factors = []
    possible_primes = sieve_eratosthenes(ceil(sqrt(n)))
    for prime in possible_primes:
        exp = 0
        while n % prime == 0:
            exp += 1
            n = n // prime
        if exp != 0:
            factors.append((prime, exp))
    if n != 1:
        return factors + [(n, 1)]
    return factors

def factor_all(b):
    '''
        Factor all numbers <= b.
        Returns a dictionary of dicts whose keys are the numbers 2 to b
        and the dictionary the prime factors together with their exponents.
        Only use this for small b as O(b)...
    '''
    factor_list = defaultdict(dict)
    for i in range(2, b + 1):
        if not factor_list[i]:
            for j in range(1, b // i + 1):
                if j % i == 0:
                    factor_list[j * i][i] = factor_list[j][i] + 1
                else:
                    factor_list[j * i][i] = 1
    return factor_list


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
    return prod((p**(e + 1) - 1) // (p - 1) for p, e in factors) - n


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
    abundant_numbers = [0] * (n + 1)
    for k in range(2, n + 1):
        if not abundant_numbers[k] and is_abundant(k):
            for i in range(k, n + 1, k):
                abundant_numbers[i] = 1
    return abundant_numbers
