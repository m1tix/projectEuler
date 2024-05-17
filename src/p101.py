from math import factorial, comb

def problem(f):
    '''
        Returns the sum of the FITs for a polynomial f. Note that this is simply
        the lagrange polynomial of all degrees less than degree(d)

        Solved with sage first:
            R.<x> = PolynomialRing(QQ, 'x')
            f = cyclotomic_polynomial(22)
            curr = 0
            for k in range(1, f.degree() + 1):
                curr += (R.lagrange_polynomial([(n, f(n) for n in range(1, k + 1))]))(k+1)

        One can also easily deduce the following formula: given a function f of degree d:
        the sum of the FITs for f is given by

            sum_{k=1}^{d-1} sum_{j=1}^k (-1)^(k-j) * f(j) * binomial(k, j - 1)

        Dont want to completely derive this here, but can be easily derived by writing the
        lagrange polynomial explicitly in terms of the lagrange basis and then noticing
        that many terms cancel each other out, or are known quantities in combinatorics.
    '''
    val = lambda func, n: sum(func[i] * n ** (len(func) - i - 1) for i in range(len(func)))
    curr = 0
    for k in range(1, len(f)):
        curr += sum((-1)**(k - j) * val(f, j) * comb(k, j - 1) for j in range(1, k + 1))
    return curr


if __name__ == "__main__":
    print(problem([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]))
