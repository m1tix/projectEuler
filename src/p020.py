from math import factorial


def problem(n):
    '''
        Returns the sum of the digits of n! (BRUTEFORCE BABY)
    '''
    return sum(map(int, str(factorial(n))))


if __name__ == "__main__":
    print(problem(100))
