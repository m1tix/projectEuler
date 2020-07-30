import utils


def problem010(n):
    '''
        Returns the sum of the first n primes
    '''
    return sum(utils.sieve_eratosthenes(n))


def problem011(grid):
    '''
        Returns the greatest product of four adjacent numbers in some direction
        of the grid.
    '''


def problem012(bound):
    '''
        Returns the smallest triangle number for which the number of divisors
        is bigger or equal to bound.
    '''


if __name__ == "__main__":
    print(problem012(100))
