from utils import utils

def problem(b):
    '''
        Returns the smallest prime p <= b that is the sum of
        the most consecutive primes. 
        For HackerRank: Dont calculate all primes up to 10 ** 12,
            but first determine how many primes are necessary a priori (< 15mil?).
    '''
    # Bad form: much better to only loop once, but then 
    # the code later on will be uglier, so I let this one slide
    is_prime = utils.sieve_eratosthenes_raw(b)
    primes = [i for i, prime in enumerate(is_prime) if prime]
    # determine the maximum length of consecutive primes
    max_length = 0
    while sum(primes[:max_length]) <= b:
        max_length += 1
    # starting witht he maximum length, loop over all possible consecutive primes
    # of length i and stop when we hit some prime.
    for i in range(max_length, 1, -1):
        j = 0
        while sum(primes[j: j + i]) <= b:
            if is_prime[sum(primes[j : j + i])]:
                return sum(primes[j : j + i])
            j += 1

if __name__ == "__main__":
    print(problem(10 ** 6))
