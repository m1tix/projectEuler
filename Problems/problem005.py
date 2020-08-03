from math import gcd


def problem005(n):
    '''
        Returns the smallest integer divisible by {1,..,n}
    '''
    multiple = 1
    for i in range(2, n+1):
        multiple = multiple*i//gcd(i, multiple)
    return multiple


if __name__ == "__main__":
    print(problem005(20))
