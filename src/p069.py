def problem():
    '''
        Returns the smallest value of n <= 10 ** 6 such that n / phi(n)
        is maximal. Done by hand:
            n / phi(n) = 1 / (prod_{p | n}(1 - 1/p))
        so this is maximal if and only if
            prod_{p | n} (1 - 1/p)
        is minimal. Such a product is clearly minimized if n is divisible
        by a large number of primes. Hence a first guess would be to take the product n
        of all the smallest primes such that n does not exceed 10 ** 6.
        This will be
            2 * 3 * 5 * 7 * 11 * 13 * 17
        which is actually the answer :). Same approach works for HackerRank.
    '''
    return 2 * 3 * 5 * 7 * 11 * 13 * 17

if __name__ == "__main__":
    print(problem())
