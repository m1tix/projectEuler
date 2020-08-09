from math import log, ceil
from Utils import utils


def problem007(n):
    '''
        Returns the n-th prime through sieve of eratosthenes. The given bound
        is a corollary of the prime number theorem (if n >= 6, that is)
    '''
    primeList = utils.sieve_eratosthenes(ceil(n * log(n) + n * log(log(n))))
    return primeList[n - 1]


if __name__ == "__main__":
    print(problem007(10001))
