from math import sqrt, floor, log10

def problem(b, d):
    '''
        Return the sum of the first d digits of all irrational
        square roots n <= b.

        Idea is simple: compute the integer square root of

            a := n * 10 ** (2 ** d)

        with Newton-Raphson applied to x^2 - a = 0. This yields

            x_{k+1} = (x_k + a/x_k) / 2

        for some x_0 > 0 with stopping condition x_{k+1} = x_{k}.
        We pick x_0 = 10 ** d as our starting position. One can speed up the computation
        by only considering primes, but not sure if it is that much faster

        NOTE: for HackerRank set sys.set_int_max_str_digits(20000)
    '''
    newton_raphson = lambda x, n: (x + n // x) // 2 
    tot = 0
    for n in range(2, b + 1):
        sqrt_n = sqrt(n)
        if int(sqrt_n) == sqrt_n:
            continue
        digits = d - floor(log10(sqrt_n)) - 1
        target = n * 10 ** (2 * digits)
        x_prev = 0
        x_next = 10 ** digits
        while x_next != x_prev:
            x_prev, x_next = x_next, newton_raphson(x_next, target)
        tot += sum(int(k) for k in str(x_next))
    return tot


if __name__ == "__main__":
    print(problem(100, 100))
