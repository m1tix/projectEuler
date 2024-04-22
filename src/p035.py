from utils import utils


def problem(n):
    '''
        Returns the number of circular prime numbers below n. A prime is
        circular if all its rotations are prime. Note that n should be smaller
        than 10**6 because I hardcoded it this way.
        Can be optimized to only loop over the digits [1,3,7,9], but I am too
        lazy at the moment
    '''

    def rotation(p):
        '''
            Returns a list of all the rotations of the given number p.
        '''
        p = str(p)
        return [int(p[n:] + p[:n]) for n in range(len(p))]

    count = 0
    raw_primes = utils.sieve_eratosthenes_raw(n)
    for p, is_prime in enumerate(raw_primes):
        if is_prime:
            rotation_list = rotation(p)
            if all(raw_primes[r] for r in rotation_list):
                count += 1
    return count


if __name__ == "__main__":
    print(problem(10**6))
