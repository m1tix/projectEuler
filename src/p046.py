from utils import utils
from math import sqrt, floor

def problem(bound):
    '''
        Returns the smallest odd composite number <= bound that
        cannot be written as a sum of a prime and twice a square.
        Returns None if such a number does not exists
    '''
    is_prime = utils.sieve_eratosthenes_raw(bound)
    for k in range(3, bound, 2):
        if is_prime[k]:
            continue
        for i in range(1, floor(sqrt(k / 2)) + 1):
            if is_prime[k - 2 * i ** 2]:
                break
        else:
            return k
    return None

if __name__ == "__main__":
    print(problem(10000))
