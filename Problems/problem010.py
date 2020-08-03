from Utils import utils


def problem010(n):
    '''
        Returns the sum of the first n primes
    '''
    return sum(utils.sieve_eratosthenes(n))


if __name__ == "__main__":
    print(problem010(2*10**6))
