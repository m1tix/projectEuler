def problem001(n):
    '''
        Returns the sum of multiples of 3 or 5 below n
    '''
    def sfn(n):
        return int(n * (n + 1))

    return (sfn((n - 1) // 3) * 3 + sfn((n - 1) // 5) * 5 - sfn(
        (n - 1) // 15) * 15) >> 1


if __name__ == "__main__":
    print(problem001(1000))
