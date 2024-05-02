from math import factorial

def binomial(n, r):
    '''
        n choose r
    '''
    return factorial(n) / (factorial(r) * factorial(n - r))

def problem(N, b):
    '''
        Return the count of how many binomials n choose r (with 1 <= n <= N)
        exceed the given bound b > 1.

        Some binomial identities can be used, but this thing is speedy enough as is.
    '''
    count = 0
    for n in range(1, N + 1):
        for r in range(0, n // 2 + 1):
            if binomial(n, r) > b:
                count += 2
                if n % 2 == 0 and r == n // 2:
                    count -= 1
    return count


if __name__ == "__main__":
    print(problem(100, 10 ** 6))
