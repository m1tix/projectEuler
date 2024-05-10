from math import floor, sqrt

from utils import utils


def problem(b):
    '''
        Return the count of numbers <= b that can be expressed as a
        sum of a prime square, cube and fourth power.

        Just bruteforce??? (and binary search in HR)
    '''
    primes = utils.sieve_eratosthenes(floor(sqrt(b)))
    valid_nums = set()
    for p in primes:
        for q in primes:
            n = p ** 2 + q ** 3
            if n >= b:
                break
            for r in primes:
                if n + r ** 4 >= b:
                    break
                valid_nums.add(n + r ** 4)
    return len(valid_nums)


if __name__ == "__main__":
    print(problem(50 * 10 ** 6))

