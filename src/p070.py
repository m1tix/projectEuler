from math import sqrt, ceil

from utils import utils


def is_permutation(n, m):
    '''
        Returns True if the number n is a permutation of m. False otherwise
    '''
    return all(str(n).count(c) == str(m).count(c) for c in str(n))


def problem(b):
    '''
        Returns a number 1 < n < b for which phi(n) is a permutation of n and n / phi(n) is
        minimal.

        Observations:
            - Similar to problem 69, n / phi(n) is minimal iff n is prime or n is divisible by small number of big primes.
            - n cannot be prime since n and n - 1 are never each other permutations.
            - So for n / phi(n) it has to be divisible by two distinct large primes.
            - Idea: sieve up to sqrt(b) and take two primes at a time to check property.
            - If n is divisible by only two large primes, say p and q, then
                phi(n) = (p - 1)(q - 1).
    '''
    primes = utils.sieve_eratosthenes(ceil(2 * sqrt(b)))
    curr = (0, 10 ** 10)
    for i, p in enumerate(primes):
        for q in primes[i:]:
            n = p * q
            if n > b:
                continue
            m = (p - 1) * (q - 1)
            if is_permutation(n, m) and n / m < curr[1]:
                curr = (n, n / m)
    return curr[0]

if __name__ == "__main__":
    print(problem(10 ** 7))
