def problem(n):
    '''
        Returns the difference between the sum of the first n squares and the
        square of the sum of the first n integers
    '''
    sum1 = n * (n + 1) * (2 * n + 1) // 6
    sum2 = n * (n + 1) // 2

    return abs(sum1 - sum2**2)


if __name__ == "__main__":
    print(problem(100))
