from itertools import permutations
from math import floor, log10

from utils import utils


def problem(m):
    '''
        Returns the largest n-digit pandigital prime smaller than m. Note there are no 8-digit
        or 9-digit pandigital primes: The sum of the digits of 8-digit and 9-digit
        pandigital numbers are divisible by 3, namely 36 and 45, respectively, thus
        they are divisble by 3.
    '''
    to_number = lambda x: sum(10**(len(x) - i - 1) * x[i]
                              for i in range(len(x)))
    digits = floor(log10(m)) + 1
    if digits > 7:
        digits = 7
    not_found = True
    largest_prime = -1
    while not_found and digits > 0:
        candidates = permutations(range(1, digits + 1), digits)
        for p in map(to_number, candidates):
            if utils.miller_rabin(p) and m >= p > largest_prime:
                largest_prime = p
                not_found = False
        digits -= 1
    return largest_prime

if __name__ == "__main__":
    print(problem(10 ** 10 - 1))
