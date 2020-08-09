from Utils import utils


def problem012(bound):
    '''
        Returns the smallest triangle number for which the number of divisors
        is bigger or equal to bound. Note that n and n + 1 are always
        relatively prime (or else a common prime factor divides 1)
    '''
    n = 1
    totalProd = utils.number_divisors(n * (n + 1) >> 1)
    while totalProd <= bound:
        n += 1
        if n % 2 == 0:
            prod1 = utils.number_divisors(n >> 1)
            prod2 = utils.number_divisors(n + 1)
        else:
            prod1 = utils.number_divisors(n)
            prod2 = utils.number_divisors((n + 1) >> 1)
        totalProd = prod1 * prod2
    return n * (n + 1) >> 1


if __name__ == "__main__":
    print(problem012(500))
