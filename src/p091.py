from math import ceil, gcd, floor


def problem(k):
    '''
        Returns the number of right triangles where the coordinates of the vertices
        are all positive numbers bounded by k and where one vertex is (0, 0).

        First observe that there are 3k^2 triangles whose right corner
        lies on either the x-axis or the y-axis: If the right corner is (0, 0)
        then there are k options for either points, totalling k^2 options. Similarly,
        if the right corner is on the x-axis (or y-axis) (not equal to (0, 0))
        then there are k options for the last vertex.

        Now suppose that P = (x1, y1) is the right corner with 1 <= x1, y1 <= k.
        Take the perpendicular line l of the line through (0, 0) and P at the point P

            l : -x1/y1 (x - x1) + y1

        Any third point (x, y) of the triangle must lie on this line. Equivalently:

            x1 x + y1 y = x1^2 + y1^2

        , i.e.
            
            x = x1 + y1 * n/(x1, y1)    and     y = y1 - x1 * n / (x1, y1)

        for all integers n. By symmetry we may as well only count the points above
        the line through (0, 0) and P, i.e. x1 < x <= k and 0 <= y < x. We thus
        obtain a bound on n:

            1 <= n <= min(y1/x1 * (x1, y1), (k - x1)/y1 * (x1, y1))

        It might be possible to abuse more symmetry: (x1, y1) is equivalent
        to (y1, x1), but I am unsure when (k - x1)/y1 < y1/x1 holds for y1 <= x1?
    '''

    res = 3 * k ** 2
    for x1 in range(1, k + 1):
        for y1 in range(1, k + 1):
            d = gcd(x1, y1)
            # cannot multiply by d after min, precision bugs
            res += 2 * floor(min(d * y1 / x1, d * (k - x1) / y1))
    return res


if __name__ == "__main__":
    print(problem(50))

