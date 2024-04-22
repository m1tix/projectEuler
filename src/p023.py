from math import ceil

from utils import utils


def problem():
    '''
        Returns the sum of all the numbers which are not the sum of two
        abundant numbers.
    '''
    B = 28123
    abundants = [i for i, a in enumerate(utils.generate_abundant(B)) if a]
    abundants_sum = [0] * (B + 1)
    for pos, i in enumerate(abundants):
        for j in abundants[pos:]:
            if i + j <= B:
                abundants_sum[i + j] = 1
            else:
                break
    return sum(i for i, a in enumerate(abundants_sum) if not a)


def problem_hackerrank(n):
    '''
        Returns True if n is a sum of two abundant numbers and False otherwise.
    '''
    if n > 28123:
        return False
    abundants = utils.generate_abundant(n)
    for k in range(1, ceil(n / 2) + 1):
        if abundants[k] and abundants[n - k]:
            return True
    return False


if __name__ == "__main__":
    print(problem())
