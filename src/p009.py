from math import ceil


def problem(n):
    '''
        Returns the largest product 'abc' of all pythagorean triples (a,b,c)
        such that a + b + c = n. Returns -1 if there does not exists such
        triple. Note that the problem given in project Euler can be done by
        hand, but this function can be used to solve the Hackerrank version
    '''
    if n % 2:
        return -1
    triples = []
    for a in range(3, ceil(n / 3) + 1):
        for c in range(ceil(n / 3) + 1, ceil(n / 2) + 1):
            b = n - a - c
            if a**2 + b**2 == c**2:
                triples.append((a, b, c))
    if triples:
        return max(d[0] * d[1] * d[2] for d in triples)
    return -1


if __name__ == "__main__":
    print(problem(1000))
