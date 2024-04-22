from utils import utils


def problem(n):
    '''
        Returns a list [l, (a,b)] where a and b are integers bounded by n such
        that x^2+ax+b generates l consecutive primes starting with x = 0. Oh,
        also returns the largest possible l.
        Notes: (assuming n is at least bigger than 2)
            - b has to be prime
            - if b is 2, i.e. even, then a should be even since a + b + 1 has
            to be prime. If b is an odd prime, then a should be odd for
            the same reason. Also, a might be prime as well?
            - if n = 1, then a + b + 1 has to be prime hence looping over all
            primes p such that a = p - b + 1 lies in [-n, n] is sufficient.
    '''

    def consecutive(a, b):
        '''
            Returns the number of consecutive primes in x^2+ax+b starting with
            x = 0
        '''
        x = -1
        length = -1
        is_prime = True
        while is_prime:
            x += 1
            length += 1
            num = x**2 + a * x + b
            if num < 0:
                break
            if num < 2 * n:
                # this is why raw is used instead of normal sieve
                is_prime = cached_primes[num]
            else:
                is_prime = utils.miller_rabin(num)
        return length

    curr_max = [0, (0, 0)]
    cached_primes = utils.sieve_eratosthenes_raw(2 * n)
    for b, prime1 in enumerate(cached_primes[:n]):
        if prime1:
            for p, prime2 in enumerate(cached_primes):
                a = p - (b + 1)
                if prime2 and abs(a) < n:
                    consec_primes = [consecutive(a, b), (a, b)]
                    if consec_primes[0] >= curr_max[0]:
                        curr_max = consec_primes
    return curr_max


if __name__ == "__main__":
    print(problem(10**3))
