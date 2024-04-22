from math import ceil, log


def problem(n):
    '''
        Returns the index of the first fibonacci number that contains n digits
    '''
    if n < 2:
        return 1
    fib = [1, 1]
    k = 2
    digits = 1
    while digits < n:
        k += 1
        new_fib = fib[0] + fib[1]
        fib = [fib[1], new_fib]
        digits = ceil(log(new_fib, 10))
    return k


if __name__ == "__main__":
    print(problem(1000))
