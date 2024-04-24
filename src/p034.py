from itertools import combinations_with_replacement as cwr
from math import factorial


def problem():
    '''
        Returns the sum of all numbers which are equal to the sum of the
        factorial of their digits. See problem030 for an almost equivalent
        problem with a similar algorithm
    '''

    def convert(num):
        '''
        Convers an integer to an ordered tuple of its digits
        '''
        digit_list = []
        while num != 0:
            digit_list.append(num % 10)
            num = num // 10
        return tuple(sorted(digit_list))

    total = 0
    for n in range(2, 7):
        for perm in cwr(range(10), n):
            digit_sum = sum(factorial(d) for d in perm)
            digit_tuple = convert(digit_sum)
            if digit_tuple == perm:
                total += digit_sum
    return total


if __name__ == "__main__":
    print(problem())
