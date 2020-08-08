from Utils import utils


def problem21(n):
    '''
        Returns the sum of all amicable numbers under n. Two unequal numbers
        a and b are considered to be amicable when sigma(a) = b
        and sigma(b) = a, where sigma denotes the the sum-of-divisors function
    '''
    amicableSum = 0
    for k in range(n, 1, -1):
        divk = utils.sum_divisors(k)
        if divk > k:
            if utils.sum_divisors(divk) == k:
                if divk > n:
                    amicableSum += k
                else:
                    amicableSum += divk + k
    return amicableSum


if __name__ == "__main__":
    print(problem21(10000))
