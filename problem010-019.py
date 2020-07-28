import utils


def problem010(n):
    # returns the sum of the first n primes
    return sum(utils.sieve_eratosthenes(n))


print(problem010(2*10**6))
