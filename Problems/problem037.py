from collections import deque
from math import ceil, log

from Utils import utils


def problem037(n):
    '''
        Returns the sum of left-and-right truncable prime numbers who do not
        exceed 10 <= n <= 10^6. Formally, 2, 3, 5 and 7 are
        left-and-right truncable primes, but project euler does not consider
        them to be.
    '''
    def is_left_truncable(n):
        '''
            Returns True if n is left truncable and False otherwise
        '''
        bound = ceil(log(n, 10))
        for k in range(1, bound):
            if not utils.miller_rabin(n % 10**(bound - k)):
                return False
        return True

    def right_truncable(n):
        '''
            Returns a list of all right truncable numbers smaller than n.
        '''
        prefix = deque([2, 3, 5, 7])
        suffixes = [1, 3, 7, 9]
        total = []
        halt = False
        while not halt:
            current_prefix = prefix.popleft()
            for s in suffixes:
                poss_prime = current_prefix * 10 + s
                if poss_prime >= n:
                    halt = True
                    break
                if utils.miller_rabin(poss_prime):
                    total.append(poss_prime)
                    prefix.append(poss_prime)
        return total

    candidates = right_truncable(n)
    final_sum = 0
    for candidate in candidates:
        if is_left_truncable(candidate):
            final_sum += candidate
    return final_sum


if __name__ == "__main__":
    print(problem037(24))
