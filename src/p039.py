from math import floor, gcd, sqrt


def problem(p):
    '''
        Returns a number 1 <= q <= p that has the largest number of
        pythogorean triples summing to q.
        One can generate all primitive pythogorean triples by iterating
            a = r^2 - s^2, b = 2rs, c = r^2 + s^2
        with r,s coprime with one of them even. We can then simply loop over all
        multiples of our primitive pythogorean triples
    '''
    pythagorean_triples = []
    res = [0] * (p + 1)
    is_valid = lambda x, y: gcd(x, y) == 1 and not (x % 2 & y % 2)
    for r in range(1, floor(sqrt(p)) + 1):
        for s in range(1, r):
            if is_valid(r, s):
                triple = (r**2 - s**2, 2 * r * s, r**2 + s**2)
                # If bound on s can be tighter then this statement
                # is unnecessary.
                if sum(triple) <= p:
                    pythagorean_triples.append(triple)
    for triple in pythagorean_triples:
        c = sum(triple)
        for k in range(1, p // c + 1):
            res[k * c] += 1
    return res.index(max(res))


if __name__ == "__main__":
    print(problem(1000))
