from math import log, floor


def problem(n):
    '''
        Returns the n-th digit in the Champernowne constant.
    '''
    if n <= 9:
        return n
    t = floor(log(n, 10))
    k = 10**t * t - (10**t - 1) // 9
    # ugly as hell, but i cant seem to fix it
    while n - k < 0:
        k -= 9 * 10**(t - 1) * t
        t -= 1
    b = (n - k) / (t + 1)
    print((t + 1) * (b - int(b)), b)
    print(n - k, t)


if __name__ == "__main__":
    print(problem(1000))
