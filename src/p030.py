from itertools import combinations_with_replacement as cwr


def problem(n):
    '''
        Returns the sum of all the numbers which can be written as the sum of
        n-th powers of their digits, where n is greater than 3. The function
        first determines all the possible configurations of digits with
        combinations_with_replacement in itertools. It subsequently calculates
        the sum of those digits to the power n and determines whether this is
        equal to the corresponding configuration.

        With this method, this function can calculate sum of all numbers that
        can be written as the 10-th powers of their digit in less than a second
    '''

    def convert(num):
        '''
            Convert an integer to an ordered tuple of its digits padded
            by zeros. While this conversion can be done with the str() function
            ,this method is faster when n gets larger.
        '''
        digit_list = []
        while num != 0:
            digit_list.append(num % 10)
            num = num // 10
        return tuple([0] * (n - len(digit_list) + 1) + sorted(digit_list))

    total = 0
    poss_digits = cwr(range(10), n + 1)
    for perm in poss_digits:
        sum_digits = sum(d**n for d in perm)
        digit_tuple = convert(sum_digits)
        if sum_digits > 1 and digit_tuple == perm:
            total += sum_digits
    return total


if __name__ == "__main__":
    print(problem(5))
