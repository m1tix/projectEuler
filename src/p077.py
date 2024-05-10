from utils import utils

def problem(k, b=1000):
    '''
        Find the smallest number n <= bthat has at least prime partitions.

        One can use sage to calculate

        prod(sum(x ** (i * p) for i in range(b) if p * i <= b) for p in prime_range(b + 1))

        for some bound b and look for the smallest power which has a coefficient
        larger than 5000. This will be 77.

        Approach is like problem 31, but we take our coin values to be 
        primes up to a certain bound.
    '''
    res = [1] + [0] * b
    primes = utils.sieve_eratosthenes(b)
    for p in primes:
        for i in range(b - p+ 1):
            res[i + p] += res[i]
    for n, val in enumerate(res):
        if val >= k:
            return n, val
    return 'Increase bound b'

if __name__ == "__main__":
    print(problem(50000, b=1000))
