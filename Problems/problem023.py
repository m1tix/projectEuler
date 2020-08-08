from math import ceil
from Utils import utils


def problem023():
    '''
        Returns the sum of all the numbers which are not the sum of two
        abundant numbers.
    '''
    B = 28123
    abundantNumbers = [i for i, a in enumerate(utils.generate_abundant(B)) if
                       a]
    abundantSum = [0]*(B+1)
    for pos, i in enumerate(abundantNumbers):
        for j in abundantNumbers[pos:]:
            if i + j <= B:
                abundantSum[i+j] = 1
            else:
                break
    return sum(i for i, a in enumerate(abundantSum) if not a)


def problem023_hackerrank(n):
    '''
        Returns True if n is a sum of two abundant numbers and False otherwise.
    '''
    if n > 28123:
        return False
    abundantNumbers = utils.generate_abundant(n)
    for k in range(1, ceil(n/2) + 1):
        if abundantNumbers[k] and abundantNumbers[n-k]:
            return True
    return False


if __name__ == "__main__":
    print(problem023())
