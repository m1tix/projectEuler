from collections import defaultdict
from functools import reduce
from itertools import combinations
from math import floor, log10

from utils import utils


def is_concatenation_prime(p, q):
    '''
        Returns True if both concatenations of p and q is prime, False otherwise
    '''
    # from my own benchmarks it seems that this is *slightly* faster than
    # the naive int(str(n) + str(m))
    conc1 = p * (10 ** (floor(log10(q)) + 1)) + q
    conc2 = q * (10 ** (floor(log10(p)) + 1)) + p
    return utils.miller_rabin(conc1) and utils.miller_rabin(conc2)

def problem(k, b=10000):
    '''
        Return the lowest sum of k primes for which any pair of prime among these k primes
        concatenate (in any manner) to another prime. This function will only look at the
        primes below b. If there does not exists such a collection of k primes, then the program will
        return None. So increase b :)
    '''
    prime_relations = defaultdict(set)
    primes = utils.sieve_eratosthenes(b)[1:] # dont care about 2.
    in_loop = 0
    found = 4 * b
    for i, p in enumerate(primes):
        for q in primes[:i]:
            if is_concatenation_prime(p, q):
                prime_relations[p].add(q)
                prime_relations[q].add(p)
        if len(prime_relations[p]) >= k - 1:
            in_loop += 1
            candidate_found = False
            for subset in map(set, combinations(prime_relations[p], k - 1)):
                if len(set.intersection(*(prime_relations[j] | {j} for j in subset))) >= k:
                    # We found a candidate, but because sets are unordered it need not be minimal
                    new_sum = sum(subset) + p
                    candidate_found = True
                    if new_sum < found:
                        found = new_sum
            if candidate_found:
                return found, in_loop
    return None


if __name__ == "__main__":
    print(problem(5))
