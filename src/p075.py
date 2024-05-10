from math import floor, gcd, sqrt


def problem(d):
    '''
        Returns the number of positive integers n <= d which can only
        be represented as a perimeter of one pythagorean triple.

        Exact same approach as problem 39: generate all primitive pythagorean triplets
        and then loop over the multiples of each pythagorean triplet. I have since tightened
        the bound on s such that the sum check is unnecessary, which made it ~1.5x faster.
    '''
    res = [0] * (d + 1)
    for r in range(1, floor(sqrt(d)) + 1):
        for s in range(1 + r % 2, min(r, floor(sqrt(d - r ** 2)) + 1), 2):
            if gcd(r, s) == 1:
                triple = (r**2 - s**2, 2 * r * s, r**2 + s**2)
                c = sum(triple)
                for k in range(1, d // c + 1):
                    res[k * c] += 1
    real_res = [0] * (d + 1)
    for i, k in enumerate(res):
        if i == 0:
            continue
        if k == 1:
            real_res[i] = real_res[i - 1] + 1
        else:
            real_res[i] = real_res[i - 1]
    return real_res

if __name__ == "__main__":
    print(problem(15 * 10 ** 5)[-1])
