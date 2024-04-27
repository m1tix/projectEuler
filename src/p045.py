from math import sqrt

def is_pentagonal(n):
    '''
        Returns true if n is pentagonal
    '''
    t = (sqrt(24 * n + 1) + 1) / 6
    # kinda lazy
    # can also do sqrt(24 * n + 1) in Z and sqrt(24 * n + 1) = 5 mod 6.
    return t == int(t)

def problem():
    '''
        Returns the second triangular number that is both
        pentagonal and hexagonal. Note that the n-th hexagonal number
        is the (2n - 1)-th triangular number.
    '''
    n = 144
    while not is_pentagonal(n * (2 * n - 1)):
        n += 1
    return n * (2 * n - 1)


if __name__ == "__main__":
    print(problem())
