from utils import utils

def problem(k):
    '''
        Return the side length n of the square spiral for which the ratio
    along both diagonals first falls below 0 < k < 1. b controls the bound
    for the primes generated, i.e. p <= b for all primes p.

    Some observations:
        - Side lengths n can only be odd.
        - Given side length of n, its (nontrivial) values on the diagonal is given by
            
            (n - 2)^2 + i(n-1)      for i = 1,2,3.

        - The total number of numbers lying on the some diagonal for side length n is

            2(n-1) + 1 = 2n - 1.
    '''
    total_primes = 0
    n = 3
    while True:
        for i in range(1, 4):
            if utils.miller_rabin((n - 2)**2 + i * (n - 1)):
                total_primes += 1
        if total_primes / (2 * n - 1) < k:
            return n
        n += 2
    


if __name__ == "__main__":
    print(problem(0.1))

