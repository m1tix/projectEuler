from math import ceil, log


def problem025(n):
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
        newF = fib[0] + fib[1]
        fib = [fib[1], newF]
        digits = ceil(log(newF, 10))
    return k


if __name__ == "__main__":
    print(problem025(5000))
