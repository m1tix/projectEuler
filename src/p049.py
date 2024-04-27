from itertools import permutations

from utils import utils


def problem():
    '''
        Returns the first instance (after 1487) of a 4 digit number
        n such that n + k, n + 2 * k, n + 3 * k are all prime for some 
        integer k.
    '''
    is_prime = utils.sieve_eratosthenes_raw(10 ** 4)
    # Loop over all primes which can be permuted at least 3 times
    # and find all their permutations that are prime. For these permutations
    # check if any of them are equidistance from the prime
    for n in range(1488, 10 ** 4 + 1):
        if is_prime[n] and not '0' in str(n):
            found_sums = []
            for str_k in permutations(str(n), 4):
                k = int(''.join(str_k))
                if k == n:
                    continue
                if is_prime[k] and n - k not in found_sums:
                    found_sums.append(n - k)
            if len(found_sums) < 2:
                continue
            for i, s in enumerate(found_sums):
                for j, t in enumerate(found_sums):
                    if j == i:
                        continue
                    if 2 * s == t:
                        return n, n - s, n - 2 * s

if __name__ == "__main__":
    print(problem())
