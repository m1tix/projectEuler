from Utils import utils


def problem026(n):
    '''
        Returns an integer d < n such that 1/d contains the longest recurring
        cycle in its decimal fraction part, aka its repetend length.
        Some explanation may be warranted: this problem was first solved with
        bruteforce but then I noticed that the program always returned a prime
        number. As it turns out, the repetend length L of 1/d satisfies

            10^L = 1 mod d

        In other words, L divides phi(d), Euler's totient function. It follows
        that L is maximized when d is prime and 10 is a primitive root mod d.
        Thus this function first determines all the primes up to n and
        subsequently determines the largest prime p for which 10 is a primitive
        root mod p.
    '''
    if n <= 7:
        return 3
    primeList = utils.sieve_eratosthenes(n - 1)
    maxp = 1
    for p in primeList[::-1]:
        tryList = utils.factor(p - 1)
        primRoot = True
        # Some group theory!
        # Let G be a group of order n and g an element of G.
        # If for all primes p dividing n we have that g^(n / p) is not equal
        # to the neutral element of the group, then g generates G.
        # Thus in this case it follows that 10 is a primitive root mod p
        for i, _ in tryList:
            num = pow(10, (p - 1) // i, p)
            if num == 1:
                primRoot = False
                break
        if primRoot:
            maxp = p
            break
    return maxp


if __name__ == "__main__":
    print(problem026(1000))
