def problem(b):
    '''
        Return the number of blue discs such that the total number of discs
        first exceeds b and such that the chance of picking two blue discs is precisely
        1/2.

        Done (almost completely) by hand. Let x be the number of blue discs and y
        the number of red discs. The probability of picking two blue discs is given by

            P(BB) = x/(x+y) * (x - 1)/(x + y - 1).

        Thus this is 1/2 if and only if (x + y)(x + y - 1) = 2x(x-1), which yields

            x = (sqrt(8y^2 + 1) + 2y + 1) / 2

        Hence x is an integer if and only if 8y^2 + 1 = z^2 is a square. Similar to problem 94,
        this is a Pell equation for D = 2 and we know that the fundamental unit in Z[sqrt(2)] is
        2 + sqrt(2), but it has norm -1. So the general solution is then given by even powers of
        2 + sqrt(2), or more precisely

            z_k = ((3 + 2sqrt(2))^k + (3 - 2sqrt(2))^k)/2
            y_k = ((3 + 2sqrt(2))^k - (3 - 2sqrt(2))^k) / (4sqrt(2))

        for all k in Z.  Both z_k and y_k satisfy the recurrence relation

            a_n = 6a_{n-1} - a_{n-2}

        but with different starting values: y_0 = 0, y_1 = 1, z_0 = 1, z_1 = 3.
        Since x = (2y + z + 1) / 2, it is easy to deduce that x satisfies a similar
        recurrence relation

            x_n = 6x_{n-1} - x_{n-2} - 2

        with x_0 = 1, x_1 = 3.
    '''
    xs = (1, 3)
    ys = (0, 1)
    # Might be able to optimize this:
    # given x there can only be one value of y, but
    # calculating this value of y is (I think?) more expensive
    # then simply calculating the recurrence relation for y.
    # x + y = 1/2 * (sqrt(8x^2 - 8x + 1) + 1)
    while xs[-1] + ys[-1] < b:
        xs = (xs[-1], 6*xs[-1] - xs[0] - 2)
        ys = (ys[-1], 6*ys[-1] - ys[0])
    return xs[-1]

if __name__ == "__main__":
    print(problem(10 ** 12))
