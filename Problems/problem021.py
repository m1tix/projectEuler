from Utils import utils


def problem21(n):
    '''
        Returns the sum of all amicable numbers under n. Two unequal numbers
        a and b are considered to be amicable when sigma(a) = b
        and sigma(b) = a, where sigma denotes the the sum-of-divisors function
        Oh, just generates all the amicable numbers under n because why not, it
        do be kinda inefficient tho
    '''
    amicableSum = 0
    for k in range(n, 1, -1):
        divk = utils.sum_divisors(k)
        # If a,b are amicable when a > n while b < n, is a and/or b accounted
        # for in the sum? The problem is ambigious. For now, we assume that
        # both a and b are not counted. Change the < to a > to count both a
        # and b, filter if necessary.
        if divk < k:
            if utils.sum_divisors(divk) == k:
                amicableSum += divk + k
    return amicableSum


if __name__ == "__main__":
    print(problem21(10000))
