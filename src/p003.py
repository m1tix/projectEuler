from math import gcd


def problem(n):
    '''
        Returns the largest prime factor of n >= 2. Quite overkill but whatever
    '''

    def pollard(n):
        a = 2
        A = a
        for i in range(2, n):
            A = pow(A, i, n)
            F = gcd(A - 1, n)
            if 1 < F < n:
                return F
        return n

    factors = []
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n = n >> 1
    while n != 1:
        p = pollard(n)
        factors.append(p)
        n = n // p
    return max(factors)


if __name__ == "__main__":
    print(problem(600851475143))
